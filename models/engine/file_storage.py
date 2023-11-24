#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        filter_by_class = {}
        if cls:
            for key, value in FileStorage.__objects.items():
                if value.__class__ == cls:
                    filter_by_class[key] = value
            return filter_by_class
        return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        try:
            with open(FileStorage.__file_path, 'r') as f:
                FileStorage.__objects = json.load(f)
                for key, val in FileStorage.__objects.items():
                    class_name = val['__class__']
                    FileStorage.__objects[key] = classes[class_name](**val)
        except FileNotFoundError:
            pass


    def delete(self, obj=None):
        """Deletes obj from __objects"""
        if obj:
            key = '{}.{}'.format(type(obj).__name__, obj.id)
            del FileStorage.__objects[key]


    def close(self):
        """Deserialise json objects"""
        self.reload()

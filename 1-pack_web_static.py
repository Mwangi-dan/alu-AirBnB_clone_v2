#!/usr/bin/python3
"""
script that geerates a tgz arcjive from the
contents of the web_static
folder of Airbnb Clone repo
"""


from datetime import datetime
from fabric import local
from os.path import isdir


def do_pack():
    """Generating a tgz archive"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        file_name = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except:
	    return None

-- Creata a hbnb database if it doesnt exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- Creates a new user in localhost
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- Grants hbnb_dev privileges to database
GRANT ALL PRIVILEGES on hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema TO 'hbnb_dev'@'localhost';

-- Creates a hbnb_test_db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- Creates a user hbnb_test in localhost
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- Grants all privileges on the database to hbnb_test
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
-- Grants SELECT provoleges on the database performance schema
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost'


-- Script that prepares a MySQL server for the project
-- A database hbnb_test_db
-- A new user hbnb_test (in localhost)
-- The password of hbnb_test should be set to hbnb_test_pwd
-- hbnb_test should have all privileges on the database hbnb_test_db (and only this database)
-- hbnb_test should have SELECT privilege on the database performance_schema (and only this database)
-- If the database hbnb_test_db or the user hbnb_test already exists, your script should not fail
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE DATABASE IF NOT EXISTS performance_schema;
GRANT ALL ON hbnb_test_db.* TO 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';


-- Script that prepares a MySQL server

-- Create a database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create a new user
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY hbnb_dev_pwd;

-- Grant priviledges


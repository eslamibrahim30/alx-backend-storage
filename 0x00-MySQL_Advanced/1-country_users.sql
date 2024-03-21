-- This script creates a table users.
CREATE TABLE IF NOT EXISTS users(
	id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
	email VARCHAR(256) NOT NULL UNIQUE, 
	name VARCHAR(256),
	country ENUM('US','CO','TN') NOT NULL DEFAULT 'US'
);

-- another table with a foreign key to the first table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities(
	id INT AUTO_INCREMENT PRIMARY KEY,
	state_id INT NOT NULL FOREIGN KEY REFERENCES states(id),
	name VARCHAR(256) NOT NULL);

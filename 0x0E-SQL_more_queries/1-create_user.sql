-- create user
CREATE USER IF NOT EXISTS 'user_od_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGE PRIVILEGES
ON *.*
TO 'user_od_1'@'localhost'
FLUSH PRIVILEGES;

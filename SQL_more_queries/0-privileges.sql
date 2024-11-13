-- List all priviledges
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost';
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost';

GRANT ALL PRIVILEDGES ON *.* TO 'user_0d_1'@'localhost';
GRANT ALL PRIVILEDGES ON *.* TO 'user_0d_1'@'localhost';

SHOW GRANTS FOR 'user_0d_1'@'localhost';
SHOW GRANTS FOR 'user_0d_2'@'localhost';

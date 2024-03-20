-- Task 0: Script creates a table users
-- script can be executed on any database
-- script should not fail if table already exists
CREATE TABLE If NOT EXISTS `users` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `email` VARCHAR(255) NOT NULL UNIQUE,
    `name` VARCHAR(255),
    `country` ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US'
);

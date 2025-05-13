-- Run this block if you already have a database and need to re-create it
DELETE FROM Orders;
DELETE FROM Customers;
DELETE FROM Styles;
DELETE FROM Sizes;
DELETE FROM Metals;

DROP TABLE IF EXISTS Orders;
DROP TABLE IF EXISTS Customers;
DROP TABLE IF EXISTS Styles;
DROP TABLE IF EXISTS Sizes;
DROP TABLE IF EXISTS Metals;
-- End block


-- Run this block to create the tables and seed them with some initial data
CREATE TABLE `Metals`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `metal` NVARCHAR(160) NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);

CREATE TABLE `Sizes`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `size` NVARCHAR(50) NOT NULL
);

CREATE TABLE `Styles`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `style` NVARCHAR(100) NOT NULL
);

CREATE TABLE `Customers`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `name` NVARCHAR(200) NOT NULL,
    `email` NVARCHAR(100)
);

CREATE TABLE `Orders`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `customer_id` INTEGER NOT NULL,
    `metal_id` INTEGER NOT NULL,
    `size_id` INTEGER NOT NULL,
    `style_id` INTEGER NOT NULL,
    `quantity` INTEGER NOT NULL,
    `order_date` DATE NOT NULL,
    FOREIGN KEY(`customer_id`) REFERENCES `Customers`(`id`),
    FOREIGN KEY(`metal_id`) REFERENCES `Metals`(`id`),
    FOREIGN KEY(`size_id`) REFERENCES `Sizes`(`id`),
    FOREIGN KEY(`style_id`) REFERENCES `Styles`(`id`)
);

INSERT INTO `Metals` VALUES (null, 'Gold', 1850.75);
INSERT INTO `Metals` VALUES (null, 'Silver', 27.50);
INSERT INTO `Metals` VALUES (null, 'Platinum', 950.25);
INSERT INTO `Metals` VALUES (null, 'Copper', 4.30);

INSERT INTO `Sizes` VALUES (null, 'Small');
INSERT INTO `Sizes` VALUES (null, 'Medium');
INSERT INTO `Sizes` VALUES (null, 'Large');

INSERT INTO `Styles` VALUES (null, 'Ring');
INSERT INTO `Styles` VALUES (null, 'Necklace');
INSERT INTO `Styles` VALUES (null, 'Bracelet');
INSERT INTO `Styles` VALUES (null, 'Earrings');

INSERT INTO `Customers` VALUES (null, 'John Smith', 'john.smith@email.com');
INSERT INTO `Customers` VALUES (null, 'Emma Johnson', 'emma.j@email.com');
INSERT INTO `Customers` VALUES (null, 'Michael Brown', 'mbrown@email.com');

INSERT INTO `Orders` VALUES (null, 1, 1, 2, 1, 1, '2025-05-01');
INSERT INTO `Orders` VALUES (null, 2, 2, 1, 3, 2, '2025-05-05');
INSERT INTO `Orders` VALUES (null, 3, 3, 3, 2, 1, '2025-05-08');
-- End block
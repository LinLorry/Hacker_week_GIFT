USE GIFT;

CREATE TABLE users
(
        user_id INT UNSIGNED AUTO_INCREMENT,
        PRIMARY KEY (user_id)
);

CREATE TABLE classes_first
(
        class_id TINYINT UNSIGNED AUTO_INCREMENT,
        class_name varchar(16) NOT NULL,

        PRIMARY KEY (class_id)
)CHARSET=utf8;


CREATE TABLE classes_second
(
        first_id TINYINT UNSIGNED NOT NULL, 
        class_id TINYINT UNSIGNED AUTO_INCREMENT,
        class_name varchar(16) NOT NULL,

        PRIMARY KEY (class_id),
        CONSTRAINT class_first_id FOREIGN KEY (first_id) REFERENCES classes_first (class_id)
)CHARSET=utf8;


CREATE TABLE products
(
        class_id TINYINT UNSIGNED NOT NULL,

        product_id INT UNSIGNED AUTO_INCREMENT,
        product_name varchar(64) NOT NULL,

        level TINYINT CHECK (gender IN (1,2,3,4,5,6,7,8,9)),
        price SMALLINT UNSIGNED NOT NULL,
        collect_number SMALLINT UNSIGNED,
        commentaries text,

        PRIMARY KEY (product_id),
        CONSTRAINT class_second_id FOREIGN KEY (class_id) REFERENCES classes_second (class_id)
)CHARSET=utf8;


INSERT INTO classes_first(class_name)
VALUES
('电子产品'),
('化妆品'),
('书籍');

INSERT INTO classes_second(first_id,class_name)
VALUES
(1,'手机'),
(1,'电脑'),
(2,'口红');

INSERT INTO products (class_id,product_name,level,price,collect_number)
VALUES
(1,'华为p10',8,5000,5000);

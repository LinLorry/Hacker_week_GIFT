USE GIFT;

CREATE TABLE users
(
user_id INT UNSIGNED AUTO_INCREMENT,
PRIMARY KEY (user_id)
);

CREATE TABLE classes_first
(
id TINYINT UNSIGNED AUTO_INCREMENT,
name varchar(16) NOT NULL,

PRIMARY KEY (id)
)CHARSET=utf8;


CREATE TABLE classes_second
(
f_id TINYINT UNSIGNED NOT NULL, 
id TINYINT UNSIGNED AUTO_INCREMENT,
name varchar(16) NOT NULL,

PRIMARY KEY (id),
CONSTRAINT c_s_fkey FOREIGN KEY (f_id) REFERENCES classes_first (id)
)CHARSET=utf8;


CREATE TABLE products
(
s_id TINYINT UNSIGNED NOT NULL,

id FLOAT UNSIGNED AUTO_INCREMENT,

name varchar(64) NOT NULL,
level TINYINT CHECK (gender IN (1,2,3,4,5,6,7,8,9)),
price SMALLINT UNSIGNED NOT NULL,
collect_number SMALLINT UNSIGNED,
commentaries text,

PRIMARY KEY (id),
CONSTRAINT p_fkey FOREIGN KEY (s_id) REFERENCES classes_second (id)
)CHARSET=utf8;




INSERT INTO classes_first(name)
VALUE
('电子产品'),
('化妆品'),
('书籍');

INSERT INTO classes_second(f_id,name)
VALUE
((SELECT f.id
FROM classes_first f
WHERE f.name = '电子产品'),'手机'),
((SELECT f.id
FROM classes_first f
WHERE f.name = '电子产品'),'电脑'),
((SELECT f.id
FROM classes_first f
WHERE f.name = '电子产品'),'耳机')，
((SELECT f.id
FROM classes_first f
WHERE f.name = '化妆品'),'口红'),
((SELECT f.id
FROM classes_first f
WHERE f.name = '化妆品'),'护肤品');


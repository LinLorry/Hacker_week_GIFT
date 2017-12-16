USE GIFT;

DROP TABLE users;
DROP TABLE products;
DROP TABLE classes_second;
DROP TABLE classes_first;

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

j_standard text,

top_preface varchar(256),
top_title varchar(64),

medium_preface varchar(256),
medium_title varchar(64),

low_preface varchar(256),
low_title varchar(64),


PRIMARY KEY (id),
CONSTRAINT c_s_fkey FOREIGN KEY (f_id) REFERENCES classes_first (id)
)CHARSET=utf8;


CREATE TABLE products
(
s_id TINYINT UNSIGNED NOT NULL,

id SMALLINT UNSIGNED AUTO_INCREMENT,

name varchar(64) NOT NULL,
level TINYINT CHECK (gender IN (1,2,3,4,5,6,7,8,9)),
H_price FLOAT UNSIGNED NOT NULL,
L_price FLOAT UNSIGNED NOT NULL,
title varchar(64),
commentaries text,

PRIMARY KEY (id),
CONSTRAINT p_fkey FOREIGN KEY (s_id) REFERENCES classes_second (id)
)CHARSET=utf8;


INSERT INTO classes_first(name)
VALUE
('电子产品'),
('化妆品'),
('书籍');

INSERT INTO classes_second
(f_id,name)
VALUES
((SELECT f.id
FROM classes_first f
WHERE f.name = '电子产品'),
'电脑');

INSERT INTO classes_second
(f_id,name,j_standard)
VALUE
((SELECT f.id
FROM classes_first f
WHERE f.name = '电子产品'),
'手机',
"{'first':'1. 在性能与配置上，高端手机屏幕显示效果通透、亮丽、可视角大，色彩饱和与还原度高；中低端手机屏幕显示效果一般，色彩饱和度中等。高端手机分辨率达到2560*1440（2K/ Quad HD）、4096×2160（4K/Ultra HD），屏幕超清且舒适；中端手机分辨率可达1334×750、1920*1080（1080p/FHD），屏幕清晰度高；而低端手机分辨率仅1280*720（720p/HD）。高中端手机处理器强劲，系统流畅，满足大多数专业软件与游戏运行要求；而低端手机打开基础软件不卡顿，低配置游戏运行顺畅。',
'second':'2. 在价格上，高端手机价格一般在4000以上，中端手机在2000~4000之间，低端手机在2000以下。',
'third':'3. 在外观设计上，高中端手机外观采用全面屏、曲面屏、超窄边框或双曲面，外观个性，亮点十足；而低端手机外观中规中矩。',
'fourth':'4. 在特色功能上，高中端手机电池容量大，具有快充功能。高中端手机前后摄像头像素超高，具有双摄像头，美颜效果远强于低端手机。部分高中端手机带红外线感应，可调节空调温度；带NFC功能，可作公交车或银行卡存取使用；甚至具有全网通功能，移动、联通、电信的4G均可以使用。'}"),


((SELECT f.id
FROM classes_first f
WHERE f.name = '化妆品'),
'护肤品',
"{'first':'1.	在使用效果上，高端护肤品的稳定性、安全性、有效性以及使用时的方便性和舒适度、使用后的清爽程度均为顶级，能够最大程度地满足使用者对肌肤的保湿、美白、提亮、淡斑、祛痘、细化毛孔等需求；中端护肤品在稳定性、有效性以及舒适度等参数上不若高端护肤品，但仍能较好地满足使用者对肌肤状况做出一定调整及优化的需求；普通护肤品有一部分无法适应多种肤质，无法给各种肌肤类型的用户带来较高品质的使用体验。',
'second':'2.在价格上，高端护肤品的售价几乎都在千元以上，中端护肤品的价格在200~600的区间内，而普通护肤品的价位在两百元以下。',
'third':'3.	在市场定位上，中高端护肤品的品牌形象对应的是有一定经济基础且注重保养的都市女性，而普通护肤品的品牌形象则是面向大众、经济实惠。'}");

INSERT INTO classes_second
(f_id,name,
j_standard,
top_title,
top_preface,
medium_title,
medium_preface,
low_title,
low_preface)
VALUE
((SELECT f.id
FROM classes_first f
WHERE f.name = '化妆品'),
'口红',
"{'first':'1.	在市场定位上，高端口红的品牌形象定调为奢华，社会上层女性是它们的目标客户；中端口红的品牌形象是“奢侈品中较为亲民的单品”，目标客户为追求品质生活的中产阶级女性以及广大爱美的女学生；普通口红的品牌形象为大众、亲民，市场定位为质量较好的“开架化妆品”。',
'second':'2.在使用效果上，高端口红的滋润度、显色度、保湿度均为顶尖，而中端口红略差一些，普通口红相较之下则表现得更为一般。',
'third':'3.	在价格上，高端口红的单价一般都在500RMB以上一支，中端大致为200~400RMB一支，普通口红则为几十元到一百多不等。',
'fourth':'4.在外观设计上，高端口红一般有着奢华、精心雕琢的外观，中端口红的外观则是充满设计感，而普通口红的外观则显得更加简洁、平淡。'}",
'极奢至崇，送她的唇妆当然要尽态极妍',
"一个爱美的女孩，永远都缺一支昂贵的口红。
不为其他，那支口红本身，就承载了许多
也许是独立，也许是宠溺
但不管怎么样，都是女孩们努力打造自身的写照
想要博得美人一笑？那可千万别错过下面三款口红",
'极奢至崇，送她的唇妆当然要尽态极妍',
"有什么是一支口红解决不了的
如果有
那就两支
但是，谁让地球上这么多人
我偏偏中意你呢？
不说啦，我还要给她挑口红呢",
'青春烂漫，融化那颗少女心',
"一逛逛一天
一吃一大碗
一洗一大桶
一送就一打
平价怎么了，好看不就得了"),
((SELECT f.id
FROM classes_first f
WHERE f.name = '电子产品'),
'耳机',
"{'first':'1.	在外观及配置上，高端耳机拥有精致的做工及考究的用料、符合人体工学的设计以及最大限度还原音乐本真的内部配置；中端耳机外观做工考量，配置相较于高端略逊一筹，但仍能呈现优质的高中低频音色；普通耳机在外观上并无特别之处，配置仅能满足基本通话和听音乐的功能。',
'second':'2.在用户体验上，高端耳机频响范围较宽、额定功率较大，阻抗和灵敏度也恰到好处，这就决定了它们能给用户带来顶级的听觉盛宴；中端耳机声底纯净、平衡感好、解析力好、声场刻画能力优秀、高频舒展延伸、中频透明、低频富有弹性和力度；普通耳机仅能在一定程度上还原原声。
'third':'3.在价格上，高端耳机动辄两三千，是耳机“发烧友”的追求；中端耳机多在200~900的区间内，更为追求品质音乐的“听友”所接受；普通耳机几十元到一百多元不等，最为大众所接受。'}",
'在这喧哗的世间，我想送你一隅宁静的天地',
'你塞着耳机，从我身边经过
可是音乐
将我们隔成了两个世界
我不懂频响范围、阻抗度
但我想懂你',
'在这喧哗的世间，我想送你一隅宁静的天地',
'你塞着耳机，从我身边经过
可是音乐
将我们隔成了两个世界
我不懂频响范围、阻抗度
但我想懂你',
'在这喧哗的世间，我想送你一隅宁静的天地',
'你塞着耳机，从我身边经过
可是音乐
将我们隔成了两个世界
我不懂频响范围、阻抗度
但我想懂你');

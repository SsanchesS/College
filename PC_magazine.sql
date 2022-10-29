CREATE TABLE IF NOT EXISTS user(
  id integer PRIMARY KEY AUTOINCREMENT,
  username TEXT,
  password TEXT,
  card TEXT
  );
CREATE TABLE IF NOT EXISTS online_magazine(
  id integer PRIMARY KEY AUTOINCREMENT,
  title TEXT,
  short_name TEXT
  ); 
CREATE TABLE IF NOT EXISTS product_type(
  product_type TEXT PRIMARY KEY,
  note TEXT
  ); 
CREATE TABLE IF NOT EXISTS product(
  id integer PRIMARY KEY AUTOINCREMENT,
  left_in_stock integer,
  note TEXT,
  FOREIGN KEY (id) REFERENCES product_type(product_type)
  ); 
CREATE TABLE IF NOT EXISTS manager(
  id integer PRIMARY KEY AUTOINCREMENT,
  user_id integer,
  FOREIGN KEY (user_id) REFERENCES user(id)   
  );
CREATE TABLE IF NOT EXISTS sale_product(
  transaction_code integer PRIMARY KEY AUTOINCREMENT,
  online_magazine_id INT,
  user_id integer,
  product_id integer,
  manager_id integer,
  date_and_time_of_receipt date,
  title TEXT,
  FOREIGN KEY (online_magazine_id) REFERENCES online_magazine(id),
  FOREIGN KEY (product_id) references product(id),
  FOREIGN KEY (user_id) references manager(user_id),
  FOREIGN KEY (manager_id) references manager(id)
  ); 
INSERT INTO user (username,password,card) VALUES ('Sanches','myparol3213','123-404-516');
INSERT INTO user (username,password,card) VALUES ('Manches','mynjfdsjal4213','123-404-712');
INSERT INTO user (username,password,card) VALUES ('Kukanches','myparo4214213','123-321-521');
INSERT INTO user (username,password,card) VALUES ('Zhizhanches','mypa61fas23','123-612-866');
INSERT INTO user (username,password,card) VALUES ('Jujanches','myfkhgsa6213','123-512-311');
INSERT INTO user (username,password,card) VALUES ('Shishkanches','123321','213-412-512');

INSERT INTO online_magazine (title,short_name) VALUES ("SanchoPC - Let's update your PC!","SanchoPC");

INSERT INTO product_type (product_type) VALUES ('Video_card');
INSERT INTO product_type (product_type) VALUES ('Processor');
INSERT INTO product_type (product_type,note) VALUES ('Mother','Motherboard');
INSERT INTO product_type (product_type) VALUES ('Computers');
INSERT INTO product_type (product_type) VALUES ('Monitors');

INSERT INTO product (left_in_stock) VALUES (3);
INSERT INTO product (left_in_stock) VALUES (34);
INSERT INTO product (left_in_stock) VALUES (15);
INSERT INTO product (left_in_stock) VALUES (8);
INSERT INTO product (left_in_stock) VALUES (154);

INSERT INTO manager (user_id) VALUES (1);
INSERT INTO manager (user_id) VALUES (6);
INSERT INTO manager (user_id) VALUES (5);
INSERT INTO manager (user_id) VALUES (3);
INSERT INTO manager (user_id) VALUES (2);
INSERT INTO manager (user_id) VALUES (4);

INSERT INTO sale_product (online_magazine_id,user_id,product_id,manager_id,date_and_time_of_receipt) VALUES (1,1,1,1,'19-11-2022');
INSERT INTO sale_product (online_magazine_id,user_id,product_id,manager_id,date_and_time_of_receipt) VALUES (1,5,5,3,'04-04-2020');
INSERT INTO sale_product (online_magazine_id,user_id,product_id,manager_id,date_and_time_of_receipt) VALUES (1,3,4,4,'15-02-2023');
INSERT INTO sale_product (online_magazine_id,user_id,product_id,manager_id,date_and_time_of_receipt) VALUES (1,2,2,5,'31-01-2021');
INSERT INTO sale_product (online_magazine_id,user_id,product_id,manager_id,date_and_time_of_receipt) VALUES (1,4,3,6,'09-12-2022');

SELECT * FROM user;
SELECT * FROM online_magazine;
SELECT * FROM product_type;
SELECT * FROM product;
SELECT * FROM manager;
SELECT * FROM sale_product;
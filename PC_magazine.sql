CREATE TABLE IF NOT EXISTS user(
  id integer PRIMARY KEY AUTOINCREMENT,
  username TEXT,
  card TEXT
  );
CREATE TABLE IF NOT EXISTS online_magazine(
  id integer PRIMARY KEY AUTOINCREMENT,
  title TEXT,
  short_name TEXT
  ); 
CREATE TABLE IF NOT EXISTS product(
  id integer PRIMARY KEY AUTOINCREMENT,
  title TEXT,
  note TEXT
  ); 
CREATE TABLE IF NOT EXISTS sale_product(
  transaction_code integer PRIMARY KEY AUTOINCREMENT,
  online_magazine_id INT,
  product_id INT,
  user_id INT,
  date_and_time_of_receipt date,
  title TEXT,
  FOREIGN KEY (online_magazine_id) REFERENCES online_magazine(id),
  FOREIGN KEY (product_id) references product(id),
  FOREIGN KEY (user_id) references user(id)
  ); 
INSERT INTO user (username,card) VALUES ('Санчес','123-404-516');
INSERT INTO user (username,card) VALUES ('Манчес','123-404-712');
INSERT INTO user (username,card) VALUES ('Куканчес','123-321-521');
INSERT INTO user (username,card) VALUES ('Жижанчес','123-612-866');
INSERT INTO user (username,card) VALUES ('Жужанчес','123-512-311');

INSERT INTO online_magazine (title,short_name) VALUES ('SanchoPC - Обновим твой PC!','SanchoPC');

INSERT INTO product (title) VALUES ('Видеокарта');
INSERT INTO product (title) VALUES ('Процессор');
INSERT INTO product (title,note) VALUES ('Материнка','Материнская плата');
INSERT INTO product (title) VALUES ('Компьютеры');
INSERT INTO product (title) VALUES ('Мониторы');

INSERT INTO sale_product (online_magazine_id,product_id,user_id,date_and_time_of_receipt) VALUES (1,2,1,'19-11-2022');
INSERT INTO sale_product (online_magazine_id,product_id,user_id,date_and_time_of_receipt) VALUES (1,5,5,'04-04-2020');
INSERT INTO sale_product (online_magazine_id,product_id,user_id,date_and_time_of_receipt) VALUES (1,6,5,'15-02-2023');
INSERT INTO sale_product (online_magazine_id,product_id,user_id,date_and_time_of_receipt) VALUES (1,1,4,'31-01-2021');
INSERT INTO sale_product (online_magazine_id,product_id,user_id,date_and_time_of_receipt,title) VALUES (1,3,4,'09-12-2022','Материнская плата');

SELECT * FROM user;
SELECT * FROM online_magazine;
SELECT * FROM product;
SELECT * FROM sale_product;
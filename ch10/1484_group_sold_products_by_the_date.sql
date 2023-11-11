USE leetcode;
DROP TABLE IF EXISTS Activities;
Create table If Not Exists Activities (sell_date date, product varchar(20));
Truncate table Activities;
insert into Activities (sell_date, product) values ('2020-05-30', 'Headphone');
insert into Activities (sell_date, product) values ('2020-06-01', 'Pencil');
insert into Activities (sell_date, product) values ('2020-06-02', 'Mask');
insert into Activities (sell_date, product) values ('2020-05-30', 'Basketball');
insert into Activities (sell_date, product) values ('2020-06-01', 'Bible');
insert into Activities (sell_date, product) values ('2020-06-02', 'Mask');
insert into Activities (sell_date, product) values ('2020-05-30', 'T-Shirt');

WITH date_product AS (
    SELECT sell_date,
           GROUP_CONCAT(DISTINCT product) AS products
      FROM Activities
     GROUP BY sell_date
), date_num_sold AS (
SELECT sell_date,
       COUNT(DISTINCT product) AS num_sold
  FROM Activities
 GROUP BY sell_date
)
SELECT date_num_sold.sell_date,
       date_num_sold.num_sold,
       date_product.products
  FROM date_num_sold
  JOIN date_product
    ON date_num_sold.sell_date = date_product.sell_date;
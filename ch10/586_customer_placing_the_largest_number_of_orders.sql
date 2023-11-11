USE leetcode;
DROP TABLE IF EXISTS orders;
Create table If Not Exists orders (order_number int, customer_number int);
Truncate table orders;
insert into orders (order_number, customer_number) values ('1', '1');
insert into orders (order_number, customer_number) values ('2', '2');
insert into orders (order_number, customer_number) values ('3', '3');
insert into orders (order_number, customer_number) values ('4', '3');

WITH number_of_orders_by_customer AS (
    SELECT customer_number,
           COUNT(*) AS number_of_orders
      FROM orders
     GROUP BY customer_number
)
SELECT customer_number
  FROM number_of_orders_by_customer
 WHERE number_of_orders = (SELECT MAX(number_of_orders)
                             FROM number_of_orders_by_customer);
USE leetcode;
DROP TABLE IF EXISTS Customer;
Create table If Not Exists Customer (customer_id int, name varchar(20), visited_on date, amount int);
Truncate table Customer;
insert into Customer (customer_id, name, visited_on, amount) values ('1', 'Jhon', '2019-01-01', '100');
insert into Customer (customer_id, name, visited_on, amount) values ('2', 'Daniel', '2019-01-02', '110');
insert into Customer (customer_id, name, visited_on, amount) values ('3', 'Jade', '2019-01-03', '120');
insert into Customer (customer_id, name, visited_on, amount) values ('4', 'Khaled', '2019-01-04', '130');
insert into Customer (customer_id, name, visited_on, amount) values ('5', 'Winston', '2019-01-05', '110');
insert into Customer (customer_id, name, visited_on, amount) values ('6', 'Elvis', '2019-01-06', '140');
insert into Customer (customer_id, name, visited_on, amount) values ('7', 'Anna', '2019-01-07', '150');
insert into Customer (customer_id, name, visited_on, amount) values ('8', 'Maria', '2019-01-08', '80');
insert into Customer (customer_id, name, visited_on, amount) values ('9', 'Jaze', '2019-01-09', '110');
insert into Customer (customer_id, name, visited_on, amount) values ('1', 'Jhon', '2019-01-10', '130');
insert into Customer (customer_id, name, visited_on, amount) values ('3', 'Jade', '2019-01-10', '150');

WITH sum_amount_by_visited_on AS (
    SELECT visited_on,
           SUM(amount) AS amount
      FROM Customer
     GROUP BY visited_on
     ORDER BY visited_on
), moving_sum_avg AS (
    SELECT visited_on,
           SUM(amount) OVER (ORDER BY visited_on RANGE INTERVAL 6 DAY PRECEDING) AS amount,
           SUM(amount) OVER (ORDER BY visited_on RANGE INTERVAL 6 DAY PRECEDING) / 7 AS average_amount
      FROM sum_amount_by_visited_on
)
SELECT visited_on,
       amount,
       ROUND(average_amount, 2) AS average_amount
  FROM moving_sum_avg
 WHERE visited_on >= (SELECT DATE_ADD(MIN(visited_on), INTERVAL 6 DAY)
                        FROM moving_sum_avg);
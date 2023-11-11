USE leetcode;
DROP TABLE IF EXISTS Prices;
DROP TABLE IF EXISTS UnitsSold;
Create table If Not Exists Prices (product_id int, start_date date, end_date date, price int);
Create table If Not Exists UnitsSold (product_id int, purchase_date date, units int);
Truncate table Prices;
insert into Prices (product_id, start_date, end_date, price) values ('1', '2019-02-17', '2019-02-28', '5');
insert into Prices (product_id, start_date, end_date, price) values ('1', '2019-03-01', '2019-03-22', '20');
insert into Prices (product_id, start_date, end_date, price) values ('2', '2019-02-01', '2019-02-20', '15');
insert into Prices (product_id, start_date, end_date, price) values ('2', '2019-02-21', '2019-03-31', '30');
Truncate table UnitsSold;
insert into UnitsSold (product_id, purchase_date, units) values ('1', '2019-02-25', '100');
insert into UnitsSold (product_id, purchase_date, units) values ('1', '2019-03-01', '15');
insert into UnitsSold (product_id, purchase_date, units) values ('2', '2019-02-10', '200');
insert into UnitsSold (product_id, purchase_date, units) values ('2', '2019-03-22', '30');

WITH revenue_units AS (
    SELECT Prices.product_id,
           Prices.price * UnitsSold.units AS revenue,
           UnitsSold.units
      FROM UnitsSold
      RIGHT JOIN Prices
        ON UnitsSold.product_id = Prices.product_id
     WHERE (UnitsSold.purchase_date BETWEEN Prices.start_date AND Prices.end_date) OR
           UnitsSold.units IS NULL
)
SELECT product_id,
       IFNULL(ROUND(SUM(revenue) / SUM(units), 2), 0) AS average_price
  FROM revenue_units
 GROUP BY product_id;
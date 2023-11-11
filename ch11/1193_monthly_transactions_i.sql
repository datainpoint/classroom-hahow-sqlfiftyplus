USE leetcode;
DROP TABLE IF EXISTS Transactions;
Create table If Not Exists Transactions (id int, country varchar(4), state enum('approved', 'declined'), amount int, trans_date date);
Truncate table Transactions;
insert into Transactions (id, country, state, amount, trans_date) values ('121', 'US', 'approved', '1000', '2018-12-18');
insert into Transactions (id, country, state, amount, trans_date) values ('122', 'US', 'declined', '2000', '2018-12-19');
insert into Transactions (id, country, state, amount, trans_date) values ('123', 'US', 'approved', '2000', '2019-01-01');
insert into Transactions (id, country, state, amount, trans_date) values ('124', 'DE', 'approved', '2000', '2019-01-07');

WITH aggregate_all_transactions AS (
    SELECT DATE_FORMAT(trans_date, '%Y-%m') AS month,
           country,
           COUNT(*) AS trans_count,
           SUM(amount) AS trans_total_amount
      FROM Transactions
     GROUP BY month,
              country
), aggregate_approved_transactions AS (
    SELECT DATE_FORMAT(trans_date, '%Y-%m') AS month,
           country,
           COUNT(*) AS approved_count,
           SUM(amount) AS approved_total_amount
      FROM Transactions
     WHERE state = 'approved'
     GROUP BY month,
              country
)
SELECT aggregate_all_transactions.month,
       aggregate_all_transactions.country,
       aggregate_all_transactions.trans_count,
       IFNULL(aggregate_approved_transactions.approved_count, 0) AS approved_count,
       aggregate_all_transactions.trans_total_amount,
       IFNULL(aggregate_approved_transactions.approved_total_amount, 0) AS approved_total_amount
  FROM aggregate_all_transactions
  LEFT JOIN aggregate_approved_transactions
    ON aggregate_all_transactions.month = aggregate_approved_transactions.month AND
       aggregate_all_transactions.country = aggregate_approved_transactions.country;
USE leetcode;
DROP TABLE IF EXISTS Activity;
Create table If Not Exists Activity (player_id int, device_id int, event_date date, games_played int);
Truncate table Activity;
insert into Activity (player_id, device_id, event_date, games_played) values ('1', '2', '2016-03-01', '5');
insert into Activity (player_id, device_id, event_date, games_played) values ('1', '2', '2016-03-02', '6');
insert into Activity (player_id, device_id, event_date, games_played) values ('2', '3', '2017-06-25', '1');
insert into Activity (player_id, device_id, event_date, games_played) values ('3', '1', '2016-03-02', '0');
insert into Activity (player_id, device_id, event_date, games_played) values ('3', '4', '2018-07-03', '5');

WITH first_second_login_dates AS (
    SELECT DISTINCT player_id,
           FIRST_VALUE(event_date) OVER (PARTITION BY player_id ORDER BY event_date) AS first_login_date,
           NTH_VALUE(event_date, 2) OVER (PARTITION BY player_id) AS second_login_date
      FROM Activity
), is_login AS (
    SELECT player_id,
           CASE WHEN DATEDIFF(second_login_date, first_login_date) = 1 THEN 1
                ELSE 0 END AS is_login_consecutively
      FROM first_second_login_dates
)
SELECT ROUND(SUM(is_login_consecutively) / COUNT(*), 2) AS fraction
  FROM is_login;
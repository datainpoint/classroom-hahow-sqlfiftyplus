USE leetcode;
DROP TABLE IF EXISTS Movies;
DROP TABLE IF EXISTS Users;
DROP TABLE IF EXISTS MovieRating;
Create table If Not Exists Movies (movie_id int, title varchar(30));
Create table If Not Exists Users (user_id int, name varchar(30));
Create table If Not Exists MovieRating (movie_id int, user_id int, rating int, created_at date);
Truncate table Movies;
insert into Movies (movie_id, title) values ('1', 'Avengers');
insert into Movies (movie_id, title) values ('2', 'Frozen 2');
insert into Movies (movie_id, title) values ('3', 'Joker');
Truncate table Users;
insert into Users (user_id, name) values ('1', 'Daniel');
insert into Users (user_id, name) values ('2', 'Monica');
insert into Users (user_id, name) values ('3', 'Maria');
insert into Users (user_id, name) values ('4', 'James');
Truncate table MovieRating;
insert into MovieRating (movie_id, user_id, rating, created_at) values ('1', '1', '3', '2020-01-12');
insert into MovieRating (movie_id, user_id, rating, created_at) values ('1', '2', '4', '2020-02-11');
insert into MovieRating (movie_id, user_id, rating, created_at) values ('1', '3', '2', '2020-02-12');
insert into MovieRating (movie_id, user_id, rating, created_at) values ('1', '4', '1', '2020-01-01');
insert into MovieRating (movie_id, user_id, rating, created_at) values ('2', '1', '5', '2020-02-17');
insert into MovieRating (movie_id, user_id, rating, created_at) values ('2', '2', '2', '2020-02-01');
insert into MovieRating (movie_id, user_id, rating, created_at) values ('2', '3', '2', '2020-03-01');
insert into MovieRating (movie_id, user_id, rating, created_at) values ('3', '1', '3', '2020-02-22');
insert into MovieRating (movie_id, user_id, rating, created_at) values ('3', '2', '4', '2020-02-25');

WITH user_who_rated_most AS (
    SELECT Users.name
      FROM MovieRating
      JOIN Users
        ON MovieRating.user_id = Users.user_id
     GROUP BY Users.user_id,
              Users.name
     ORDER BY COUNT(*) DESC,
              Users.name
     LIMIT 1
), movie_which_rated_highest AS (
    SELECT Movies.title
      FROM MovieRating
      JOIN Movies
        ON MovieRating.movie_id = Movies.movie_id
     WHERE MovieRating.created_at BETWEEN '2020-02-01' AND '2020-02-29'
     GROUP BY Movies.movie_id,
              Movies.title
     ORDER BY AVG(rating) DESC,
              Movies.title
     LIMIT 1
)
SELECT name AS results
  FROM user_who_rated_most
 UNION ALL
SELECT title AS results
  FROM movie_which_rated_highest;
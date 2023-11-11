USE leetcode;
DROP TABLE IF EXISTS ActorDirector;
Create table If Not Exists ActorDirector (actor_id int, director_id int, timestamp int);
Truncate table 1050ActorDirector;
insert into ActorDirector (actor_id, director_id, timestamp) values ('1', '1', '0');
insert into ActorDirector (actor_id, director_id, timestamp) values ('1', '1', '1');
insert into ActorDirector (actor_id, director_id, timestamp) values ('1', '1', '2');
insert into ActorDirector (actor_id, director_id, timestamp) values ('1', '2', '3');
insert into ActorDirector (actor_id, director_id, timestamp) values ('1', '2', '4');
insert into ActorDirector (actor_id, director_id, timestamp) values ('2', '1', '5');
insert into ActorDirector (actor_id, director_id, timestamp) values ('2', '1', '6');

SELECT actor_id,
       director_id
  FROM ActorDirector
 GROUP BY actor_id,
          director_id
HAVING COUNT(*) >= 3;
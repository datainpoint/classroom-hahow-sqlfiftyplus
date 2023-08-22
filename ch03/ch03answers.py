# 進階的 SQL 五十道練習

## 快速複習基礎的 SQL 查詢敘述

### 0301（程式題）查詢 imdb 資料庫 movies 資料表中第八至第十列的觀測值。

answer_0301 =\
"""
SELECT *
  FROM imdb.movies
 LIMIT 3
OFFSET 7;
"""

### 0302（程式題）查詢 covid19 資料庫 locations 資料表中第十三列至第十六列的觀測值。

answer_0302 =\
"""
SELECT *
  FROM covid19.locations
 LIMIT 4
OFFSET 12;
"""

### 0303（程式題）查詢 imdb 資料庫 movies 資料表中於 1994 年上映的電影。

answer_0303 =\
"""
SELECT id,
       title,
       release_year,
       rating
  FROM imdb.movies
 WHERE release_year = 1994;
"""

### 0304（程式題）查詢 covid19 資料庫 locations 資料表中台灣的資料。

answer_0304 =\
"""
SELECT id,
       country_name,
       iso2,
       iso3,
       population
  FROM covid19.locations
 WHERE country_name = 'Taiwan';
"""

### 0305（程式題）查詢 covid19 資料庫 calendars 資料表中最小的日期與最大的日期。

answer_0305 =\
"""
SELECT MIN(recorded_on) AS min_date,
       MAX(recorded_on) AS max_date
  FROM covid19.calendars;
"""

### 0306（程式題）查詢 imdb 資料庫 movies 資料表中最短的片長與最長的片長。

answer_0306 =\
"""
SELECT MIN(runtime) AS min_runtime,
       MAX(runtime) AS max_runtime
  FROM imdb.movies;
"""

### 0307（程式題）查詢 imdb 資料庫 movies 資料表中最短片長與最長片長的電影。

answer_0307 =\
"""
SELECT title,
       runtime
  FROM imdb.movies
 WHERE runtime = (SELECT MAX(runtime) FROM imdb.movies) OR
       runtime = (SELECT MIN(runtime) FROM imdb.movies);
"""

### 0308（程式題）查詢 covid19 資料庫 accumulative_cases 資料表中最小的日期與最大的日期。

answer_0308 =\
"""
SELECT DISTINCT calendars.recorded_on AS min_max_date
  FROM covid19.accumulative_cases
  JOIN covid19.calendars
    ON accumulative_cases.calendar_id = calendars.id
 WHERE accumulative_cases.calendar_id = (SELECT MIN(calendar_id) FROM covid19.accumulative_cases) OR
       accumulative_cases.calendar_id = (SELECT MAX(calendar_id) FROM covid19.accumulative_cases);
"""

### 0309（程式題）查詢 covid19 資料庫台灣的資料。

answer_0309 =\
"""
SELECT locations.country_name,
       calendars.recorded_on,
       accumulative_cases.confirmed,
       accumulative_cases.deaths
  FROM covid19.accumulative_cases
  JOIN covid19.calendars
    ON accumulative_cases.calendar_id = calendars.id
  JOIN covid19.locations
    ON accumulative_cases.location_id = locations.id
 WHERE locations.country_name = 'Taiwan';
"""

### 0310（程式題）查詢 imdb 資料庫 Top Gun: Maverick 的演員陣容。

answer_0310 =\
"""
SELECT movies.title,
       movies.release_year,
       actors.name,
       movies_actors.ord
  FROM imdb.movies_actors
  JOIN imdb.movies
    ON movies_actors.movie_id = movies.id
  JOIN imdb.actors
    ON movies_actors.actor_id = actors.id
 WHERE movies.title = 'Top Gun: Maverick'
 ORDER BY movies_actors.ord ;
"""
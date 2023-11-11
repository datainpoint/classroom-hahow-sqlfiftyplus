USE leetcode;
DROP TABLE IF EXISTS Students;
DROP TABLE IF EXISTS Subjects;
DROP TABLE IF EXISTS Examinations;
Create table If Not Exists Students (student_id int, student_name varchar(20));
Create table If Not Exists Subjects (subject_name varchar(20));
Create table If Not Exists Examinations (student_id int, subject_name varchar(20));
Truncate table Students;
insert into Students (student_id, student_name) values ('1', 'Alice');
insert into Students (student_id, student_name) values ('2', 'Bob');
insert into Students (student_id, student_name) values ('13', 'John');
insert into Students (student_id, student_name) values ('6', 'Alex');
Truncate table Subjects;
insert into Subjects (subject_name) values ('Math');
insert into Subjects (subject_name) values ('Physics');
insert into Subjects (subject_name) values ('Programming');
Truncate table Examinations;
insert into Examinations (student_id, subject_name) values ('1', 'Math');
insert into Examinations (student_id, subject_name) values ('1', 'Physics');
insert into Examinations (student_id, subject_name) values ('1', 'Programming');
insert into Examinations (student_id, subject_name) values ('2', 'Programming');
insert into Examinations (student_id, subject_name) values ('1', 'Physics');
insert into Examinations (student_id, subject_name) values ('1', 'Math');
insert into Examinations (student_id, subject_name) values ('13', 'Math');
insert into Examinations (student_id, subject_name) values ('13', 'Programming');
insert into Examinations (student_id, subject_name) values ('13', 'Physics');
insert into Examinations (student_id, subject_name) values ('2', 'Math');
insert into Examinations (student_id, subject_name) values ('1', 'Math');

WITH students_cross_join_subjects AS (
    SELECT *
      FROM Students
     CROSS JOIN Subjects
     ORDER BY student_id,
              subject_name
), before_aggregation AS (
    SELECT students_cross_join_subjects.student_id,
           students_cross_join_subjects.student_name,
           students_cross_join_subjects.subject_name,
           CASE WHEN Examinations.subject_name IS NULL THEN 0
                ELSE 1
            END AS attended_exams
      FROM students_cross_join_subjects
      LEFT JOIN Examinations
        ON students_cross_join_subjects.student_id = Examinations.student_id AND
           students_cross_join_subjects.subject_name = Examinations.subject_name
)
SELECT student_id,
       student_name,
       subject_name,
       SUM(attended_exams) AS attended_exams
  FROM before_aggregation
 GROUP BY student_id,
          student_name,
          subject_name
 ORDER BY student_id,
          subject_name;
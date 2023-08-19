import unittest
import pymysql.cursors
import argparse

class TestEnvironment(unittest.TestCase):
    def test_01_covid19_accumulative_cases(self):
        sql_statement = """SELECT * FROM covid19.accumulative_cases;"""
        with connection.cursor() as cursor:
            cursor.execute(sql_statement)
            result = cursor.fetchall()
            self.assertTrue(len(result) >= 0)
            self.assertTrue(len(result[0]) >= 0)
    def test_02_covid19_calendars(self):
        sql_statement = """SELECT * FROM covid19.calendars;"""
        with connection.cursor() as cursor:
            cursor.execute(sql_statement)
            result = cursor.fetchall()
            self.assertTrue(len(result) >= 0)
            self.assertTrue(len(result[0]) >= 0)
    def test_03_covid19_locations(self):
        sql_statement = """SELECT * FROM covid19.locations;"""
        with connection.cursor() as cursor:
            cursor.execute(sql_statement)
            result = cursor.fetchall()
            self.assertTrue(len(result) >= 0)
            self.assertTrue(len(result[0]) >= 0)
    def test_04_imdb_actors(self):
        sql_statement = """SELECT * FROM imdb.actors;"""
        with connection.cursor() as cursor:
            cursor.execute(sql_statement)
            result = cursor.fetchall()
            self.assertTrue(len(result) >= 0)
            self.assertTrue(len(result[0]) >= 0)
    def test_05_imdb_directors(self):
        sql_statement = """SELECT * FROM imdb.directors;"""
        with connection.cursor() as cursor:
            cursor.execute(sql_statement)
            result = cursor.fetchall()
            self.assertTrue(len(result) >= 0)
            self.assertTrue(len(result[0]) >= 0)
    def test_06_imdb_movies(self):
        sql_statement = """SELECT * FROM imdb.movies;"""
        with connection.cursor() as cursor:
            cursor.execute(sql_statement)
            result = cursor.fetchall()
            self.assertTrue(len(result) >= 0)
            self.assertTrue(len(result[0]) >= 0)
    def test_07_imdb_movies_actors(self):
        sql_statement = """SELECT * FROM imdb.movies_actors;"""
        with connection.cursor() as cursor:
            cursor.execute(sql_statement)
            result = cursor.fetchall()
            self.assertTrue(len(result) >= 0)
            self.assertTrue(len(result[0]) >= 0)
    def test_08_imdb_movies_directors(self):
        sql_statement = """SELECT * FROM imdb.movies_directors;"""
        with connection.cursor() as cursor:
            cursor.execute(sql_statement)
            result = cursor.fetchall()
            self.assertTrue(len(result) >= 0)
            self.assertTrue(len(result[0]) >= 0)
    def test_09_imdb_movies_writers(self):
        sql_statement = """SELECT * FROM imdb.movies_writers;"""
        with connection.cursor() as cursor:
            cursor.execute(sql_statement)
            result = cursor.fetchall()
            self.assertTrue(len(result) >= 0)
            self.assertTrue(len(result[0]) >= 0)
    def test_10_imdb_writers(self):
        sql_statement = """SELECT * FROM imdb.writers;"""
        with connection.cursor() as cursor:
            cursor.execute(sql_statement)
            result = cursor.fetchall()
            self.assertTrue(len(result) >= 0)
            self.assertTrue(len(result[0]) >= 0)
            
parser = argparse.ArgumentParser(description='MySQL username and password.')
parser.add_argument('strings', metavar='N', type=str, nargs='+', help='MySQL username and password.')
args = parser.parse_args()
username = args.strings[0]
user_password = args.strings[1]
connection = pymysql.connect(host='localhost',
                             user=f"{username}",
                             password=f"{user_password}",
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
suite = unittest.TestLoader().loadTestsFromTestCase(TestEnvironment)
runner = unittest.TextTestRunner(verbosity=2)
test_results = runner.run(suite)
number_of_failures = len(test_results.failures)
number_of_errors = len(test_results.errors)
number_of_test_runs = test_results.testsRun
number_of_successes = number_of_test_runs - (number_of_failures + number_of_errors)
chapter_index = 2
chapter_name = "建立環境"
if number_of_successes == number_of_test_runs:
    print(f"恭喜您，通過「進階SQL的五十道練習」第{chapter_index}章：{chapter_name}全部{number_of_test_runs}個測試，好的開始是成功的一半！")
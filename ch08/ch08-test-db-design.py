import unittest
import pymysql.cursors
import argparse

class TestDBDesign(unittest.TestCase):
    def test_0801(self):
        with connection.cursor() as cursor:
            cursor.execute("""SELECT * FROM imdb.actors;""")
            number_of_columns = len(cursor.description)
            field_names = [i[0] for i in cursor.description]
            result = cursor.fetchall()
        self.assertTrue(number_of_columns == 3)
        self.assertCountEqual(field_names, ["id", "name", "link"])
        number_of_rows = len(result)
        self.assertTrue(number_of_rows == 16448)
    def test_0802(self):
        with connection.cursor() as cursor:
            cursor.execute("""SELECT * FROM imdb.directors;""")
            number_of_columns = len(cursor.description)
            field_names = [i[0] for i in cursor.description]
            result = cursor.fetchall()
        self.assertTrue(number_of_columns == 3)
        self.assertCountEqual(field_names, ["id", "name", "link"])
        number_of_rows = len(result)
        self.assertTrue(number_of_rows == 179)
    def test_0803(self):
        with connection.cursor() as cursor:
            cursor.execute("""SELECT * FROM imdb.movies;""")
            number_of_columns = len(cursor.description)
            field_names = [i[0] for i in cursor.description]
            result = cursor.fetchall()
        self.assertTrue(number_of_columns == 6)
        self.assertCountEqual(field_names, ["id", "title", "release_year", "runtime", "rating", "link"])
        number_of_rows = len(result)
        self.assertTrue(number_of_rows == 250)
    def test_0804(self):
        with connection.cursor() as cursor:
            cursor.execute("""SELECT * FROM imdb.movies_actors;""")
            number_of_columns = len(cursor.description)
            field_names = [i[0] for i in cursor.description]
            result = cursor.fetchall()
        self.assertTrue(number_of_columns == 4)
        self.assertCountEqual(field_names, ["id", "movie_id", "actor_id", "ord"])
        number_of_rows = len(result)
        self.assertTrue(number_of_rows == 18942)
    def test_0805(self):
        with connection.cursor() as cursor:
            cursor.execute("""SELECT * FROM imdb.movies_directors;""")
            number_of_columns = len(cursor.description)
            field_names = [i[0] for i in cursor.description]
            result = cursor.fetchall()
        self.assertTrue(number_of_columns == 4)
        self.assertCountEqual(field_names, ["id", "movie_id", "director_id", "ord"])
        number_of_rows = len(result)
        self.assertTrue(number_of_rows == 284)
    def test_0806(self):
        with connection.cursor() as cursor:
            cursor.execute("""SELECT * FROM imdb.movies_writers;""")
            number_of_columns = len(cursor.description)
            field_names = [i[0] for i in cursor.description]
            result = cursor.fetchall()
        self.assertTrue(number_of_columns == 4)
        self.assertCountEqual(field_names, ["id", "movie_id", "writer_id", "ord"])
        number_of_rows = len(result)
        self.assertTrue(number_of_rows == 841)
    def test_0807(self):
        with connection.cursor() as cursor:
            cursor.execute("""SELECT * FROM imdb.writers;""")
            number_of_columns = len(cursor.description)
            field_names = [i[0] for i in cursor.description]
            result = cursor.fetchall()
        self.assertTrue(number_of_columns == 3)
        self.assertCountEqual(field_names, ["id", "name", "link"])
        number_of_rows = len(result)
        self.assertTrue(number_of_rows == 586)
    def test_0808(self):
        with connection.cursor() as cursor:
            cursor.execute("""SELECT * FROM covid19.accumulative_cases;""")
            number_of_columns = len(cursor.description)
            field_names = [i[0] for i in cursor.description]
            result = cursor.fetchall()
        self.assertTrue(number_of_columns == 5)
        self.assertCountEqual(field_names, ["id", "calendar_id", "location_id", "confirmed", "deaths"])
        number_of_rows = len(result)
        self.assertTrue(number_of_rows == 328041)
    def test_0809(self):
        with connection.cursor() as cursor:
            cursor.execute("""SELECT * FROM covid19.calendars;""")
            number_of_columns = len(cursor.description)
            field_names = [i[0] for i in cursor.description]
            result = cursor.fetchall()
        self.assertTrue(number_of_columns == 2)
        self.assertCountEqual(field_names, ["id", "recorded_on"])
        number_of_rows = len(result)
        self.assertTrue(number_of_rows == 1461)
    def test_0810(self):
        with connection.cursor() as cursor:
            cursor.execute("""SELECT * FROM covid19.locations;""")
            number_of_columns = len(cursor.description)
            field_names = [i[0] for i in cursor.description]
            result = cursor.fetchall()
        self.assertTrue(number_of_columns == 8)
        self.assertCountEqual(field_names, ["id", "country_name", "province_name", "iso2", "iso3", "latitude", "longitude", "population"])
        number_of_rows = len(result)
        self.assertTrue(number_of_rows == 955)
    def test_0811(self):
        with connection.cursor() as cursor:
            cursor.execute("""SELECT * FROM tw_election_2020.admin_regions;""")
            number_of_columns = len(cursor.description)
            field_names = [i[0] for i in cursor.description]
            result = cursor.fetchall()
        self.assertTrue(number_of_columns == 4)
        self.assertCountEqual(field_names, ["id", "county", "town", "village"])
        number_of_rows = len(result)
        self.assertTrue(number_of_rows == 7737)
    def test_0812(self):
        with connection.cursor() as cursor:
            cursor.execute("""SELECT * FROM tw_election_2020.candidates;""")
            number_of_columns = len(cursor.description)
            field_names = [i[0] for i in cursor.description]
            result = cursor.fetchall()
        self.assertTrue(number_of_columns == 5)
        self.assertCountEqual(field_names, ["id", "party_id", "election_type", "num", "name"])
        number_of_rows = len(result)
        self.assertTrue(number_of_rows == 434)
    def test_0813(self):
        with connection.cursor() as cursor:
            cursor.execute("""SELECT * FROM tw_election_2020.legislative_at_large;""")
            number_of_columns = len(cursor.description)
            field_names = [i[0] for i in cursor.description]
            result = cursor.fetchall()
        self.assertTrue(number_of_columns == 5)
        self.assertCountEqual(field_names, ["id", "admin_region_id", "office", "party_id", "votes"])
        number_of_rows = len(result)
        self.assertTrue(number_of_rows == 327294)
    def test_0814(self):
        with connection.cursor() as cursor:
            cursor.execute("""SELECT * FROM tw_election_2020.legislative_regional;""")
            number_of_columns = len(cursor.description)
            field_names = [i[0] for i in cursor.description]
            result = cursor.fetchall()
        self.assertTrue(number_of_columns == 6)
        self.assertCountEqual(field_names, ["id", "admin_region_id", "electoral_district", "office", "candidate_id", "votes"])
        number_of_rows = len(result)
        self.assertTrue(number_of_rows == 459000)
    def test_0815(self):
        with connection.cursor() as cursor:
            cursor.execute("""SELECT * FROM tw_election_2020.parties;""")
            number_of_columns = len(cursor.description)
            field_names = [i[0] for i in cursor.description]
            result = cursor.fetchall()
        self.assertTrue(number_of_columns == 2)
        self.assertCountEqual(field_names, ["id", "name"])
        number_of_rows = len(result)
        self.assertTrue(number_of_rows == 46)
    def test_0816(self):
        with connection.cursor() as cursor:
            cursor.execute("""SELECT * FROM tw_election_2020.presidential;""")
            number_of_columns = len(cursor.description)
            field_names = [i[0] for i in cursor.description]
            result = cursor.fetchall()
        self.assertTrue(number_of_columns == 5)
        self.assertCountEqual(field_names, ["id", "admin_region_id", "office", "candidate_id", "votes"])
        number_of_rows = len(result)
        self.assertTrue(number_of_rows == 51678)
        
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
suite = unittest.TestLoader().loadTestsFromTestCase(TestDBDesign)
runner = unittest.TextTestRunner(verbosity=2)
test_results = runner.run(suite)
number_of_failures = len(test_results.failures)
number_of_errors = len(test_results.errors)
number_of_test_runs = test_results.testsRun
number_of_successes = number_of_test_runs - (number_of_failures + number_of_errors)
chapter_index = 8
chapter_name = "資料庫結構與資料表設計"
if number_of_successes == number_of_test_runs:
    print(f"恭喜您，通過「進階SQL的五十道練習」第{chapter_index}章：{chapter_name}全部{number_of_test_runs}個測試，經過這個章節的洗禮，我們正式地從 SQL 初階使用者升級為 SQL 進階使用者囉！")
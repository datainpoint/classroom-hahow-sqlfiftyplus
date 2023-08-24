import unittest
import pymysql.cursors
import argparse

class TestDDL(unittest.TestCase):
    def test_0401(self):
        connection = pymysql.connect(host='localhost',
                                     user=f"{username}",
                                     password=f"{user_password}",
                                     database="cloned_covid19",
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)
    def test_0402(self):
        with connection.cursor() as cursor:
            cursor.execute("""SELECT * FROM cloned_covid19.locations;""")
            number_of_columns = len(cursor.description)
            field_names = [i[0] for i in cursor.description]
            self.assertTrue(number_of_columns == 6)
            self.assertCountEqual(field_names, ["id", "country_name", "iso2", "iso3", "latitude", "longitude"])
    def test_0403(self):
        with connection.cursor() as cursor:
            cursor.execute("""SELECT * FROM cloned_covid19.calendars;""")
            number_of_columns = len(cursor.description)
            field_names = [i[0] for i in cursor.description]
            self.assertTrue(number_of_columns == 2)
            self.assertCountEqual(field_names, ["id", "recorded_on"])
    def test_0404(self):
        with connection.cursor() as cursor:
            cursor.execute("""SELECT * FROM cloned_covid19.accumulative_cases;""")
            number_of_columns = len(cursor.description)
            field_names = [i[0] for i in cursor.description]
            self.assertTrue(number_of_columns == 5)
            self.assertCountEqual(field_names, ["id", "calendar_id", "location_id", "confirmed", "deaths"])
    def test_0405(self):
        with connection.cursor() as cursor:
            cursor.execute("""SELECT * FROM covid19.accumulative_cases_20230309;""")
            result = cursor.fetchall()
            self.assertTrue(len(result) == 287)
            self.assertTrue(len(result[0]) == 5)
            calendar_ids = {res["calendar_id"] for res in result}
            self.assertEqual(calendar_ids, {1164})
    def test_0406(self):
        with connection.cursor() as cursor:
            cursor.execute("""SELECT * FROM covid19.locations_twn_jpn;""")
            result = cursor.fetchall()
            self.assertTrue(len(result) == 50)
            self.assertTrue(len(result[0]) == 8)
            country_names = {res["country_name"] for res in result}
            self.assertEqual(country_names, {'Taiwan', 'Japan'})
    def test_0407(self):
        with connection.cursor() as cursor:
            cursor.execute("""SELECT * FROM covid19.views_joined;""")
            result = cursor.fetchall()
            self.assertTrue(len(result) == 2)
            self.assertTrue(len(result[0]) == 4)
            country_names = [res["country_name"] for res in result]
            self.assertCountEqual(country_names, ["Taiwan", "Japan"])
    def test_0408(self):
        with connection.cursor() as cursor:
            cursor.execute("""SELECT * FROM covid19.views_left_joined;""")
            result = cursor.fetchall()
            self.assertTrue(len(result) == 287)
            self.assertTrue(len(result[0]) == 4)
    def test_0409(self):
        with connection.cursor() as cursor:
            cursor.execute("""SELECT * FROM covid19.views_right_joined;""")
            result = cursor.fetchall()
            self.assertTrue(len(result) == 50)
            self.assertTrue(len(result[0]) == 4)
            country_names = {res["country_name"] for res in result}
            self.assertEqual(country_names, {"Taiwan", "Japan"})

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
suite = unittest.TestLoader().loadTestsFromTestCase(TestDDL)
runner = unittest.TextTestRunner(verbosity=2)
test_results = runner.run(suite)
number_of_failures = len(test_results.failures)
number_of_errors = len(test_results.errors)
number_of_test_runs = test_results.testsRun
number_of_successes = number_of_test_runs - (number_of_failures + number_of_errors)
chapter_index = 4
chapter_name = "資料定義語言"
if number_of_successes == number_of_test_runs:
    print(f"恭喜您，通過「進階SQL的五十道練習」第{chapter_index}章：{chapter_name}全部{number_of_test_runs}個測試，你真的很厲害！")
import unittest
import pymysql.cursors
import argparse

class TestDML(unittest.TestCase):
    def test_0501(self):
        connection = pymysql.connect(host='localhost',
                                     user=f"{username}",
                                     password=f"{user_password}",
                                     database="cloned_covid19",
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)
    def test_0502(self):
        with connection.cursor() as cursor:
            cursor.execute("""SELECT * FROM cloned_covid19.locations;""")
            number_of_columns = len(cursor.description)
            field_names = [i[0] for i in cursor.description]
            self.assertTrue(number_of_columns == 8)
            self.assertCountEqual(field_names, 
                                  ["id", "country_name", "province_name", "iso2", "iso3", "latitude", "longitude", "population"])
            result = cursor.fetchall()
            self.assertTrue(len(result) == 955)
    def test_0503(self):
        with connection.cursor() as cursor:
            cursor.execute("""SELECT * FROM cloned_covid19.locations WHERE id = 496;""")
            result = cursor.fetchall()
            res = result[0]
            self.assertEqual(res["iso2"], "NA")
    def test_0504(self):
        with connection.cursor() as cursor:
            cursor.execute("""SELECT COUNT(*) AS number_of_rows FROM cloned_covid19.locations WHERE province_name = '';""")
            result = cursor.fetchall()
            res = result[0]
            self.assertEqual(res["number_of_rows"], 0)
    def test_0505(self):
        with connection.cursor() as cursor:
            cursor.execute("""SELECT COUNT(*) AS number_of_rows FROM cloned_covid19.locations WHERE iso2 = '';""")
            result = cursor.fetchall()
            res = result[0]
            self.assertEqual(res["number_of_rows"], 0)
    def test_0506(self):
        with connection.cursor() as cursor:
            cursor.execute("""SELECT COUNT(*) AS number_of_rows FROM cloned_covid19.locations WHERE iso3 = '';""")
            result = cursor.fetchall()
            res = result[0]
            self.assertEqual(res["number_of_rows"], 0)
    def test_0507(self):
        with connection.cursor() as cursor:
            cursor.execute("""SHOW INDEX FROM cloned_covid19.locations;""")
            result = cursor.fetchall()
            res = result[0]
            self.assertEqual(res["Table"], "locations")
            self.assertEqual(res["Key_name"], "PRIMARY")
            self.assertEqual(res["Column_name"], "id")
    def test_0508(self):
        with connection.cursor() as cursor:
            cursor.execute("""SELECT * FROM cloned_covid19.accumulative_cases;""")
            number_of_columns = len(cursor.description)
            field_names = [i[0] for i in cursor.description]
            self.assertTrue(number_of_columns == 5)
            self.assertCountEqual(field_names, 
                                  ["id", "location_id", "calendar_id", "confirmed", "deaths"])
            result = cursor.fetchall()
            self.assertTrue(len(result) == 328041)
    def test_0509(self):
        with connection.cursor() as cursor:
            cursor.execute("""SHOW INDEX FROM cloned_covid19.accumulative_cases;""")
            result = cursor.fetchall()
            tables = [res["Table"] for res in result]
            key_names = [res["Key_name"] for res in result]
            column_names = [res["Column_name"] for res in result]
            self.assertIn("accumulative_cases", tables)
            self.assertIn("PRIMARY", key_names)
            self.assertIn("id", column_names)
    def test_0510(self):
        with connection.cursor() as cursor:
            cursor.execute("""SHOW INDEX FROM cloned_covid19.accumulative_cases;""")
            result = cursor.fetchall()
            tables = [res["Table"] for res in result]
            key_names = [res["Key_name"] for res in result]
            column_names = [res["Column_name"] for res in result]
            self.assertIn("accumulative_cases", tables)
            self.assertIn("fk_accumulative_cases_locations", key_names)
            self.assertIn("location_id", column_names)

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
suite = unittest.TestLoader().loadTestsFromTestCase(TestDML)
runner = unittest.TextTestRunner(verbosity=2)
test_results = runner.run(suite)
number_of_failures = len(test_results.failures)
number_of_errors = len(test_results.errors)
number_of_test_runs = test_results.testsRun
number_of_successes = number_of_test_runs - (number_of_failures + number_of_errors)
chapter_index = 5
chapter_name = "資料操作語言"
if number_of_successes == number_of_test_runs:
    print(f"恭喜您，通過「進階SQL的五十道練習」第{chapter_index}章：{chapter_name}全部{number_of_test_runs}個測試，實在很了不起，給自己一個大大鼓勵！")
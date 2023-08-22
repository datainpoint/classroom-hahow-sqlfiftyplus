import unittest
import pymysql.cursors
from pymysql.constants import CLIENT
import argparse
from ch03answers import answer_0301
from ch03answers import answer_0302
from ch03answers import answer_0303
from ch03answers import answer_0304
from ch03answers import answer_0305
from ch03answers import answer_0306
from ch03answers import answer_0307
from ch03answers import answer_0308
from ch03answers import answer_0309
from ch03answers import answer_0310

class TestQueryRecap(unittest.TestCase):
    def test_0301(self):
        with connection.cursor() as cursor:
            cursor.execute(answer_0301)
            result = cursor.fetchall()
            self.assertTrue(len(result) == 3)
            self.assertTrue(len(result[0]) == 6)
            ids = [res["id"] for res in result]
            self.assertEqual(ids, [8, 9, 10])
    def test_0302(self):
        with connection.cursor() as cursor:
            cursor.execute(answer_0302)
            result = cursor.fetchall()
            self.assertTrue(len(result) == 4)
            self.assertTrue(len(result[0]) == 8)
            ids = [res["id"] for res in result]
            self.assertEqual(ids, [13, 14, 15, 16])
    def test_0303(self):
        with connection.cursor() as cursor:
            cursor.execute(answer_0303)
            result = cursor.fetchall()
            self.assertTrue(len(result) == 5)
            self.assertTrue(len(result[0]) == 4)
            ids = [res["id"] for res in result]
            self.assertEqual(ids, [1, 8, 11, 38, 39])
    def test_0304(self):
        with connection.cursor() as cursor:
            cursor.execute(answer_0304)
            result = cursor.fetchall()
            self.assertTrue(len(result) == 1)
            self.assertTrue(len(result[0]) == 5)
            ids = [res["id"] for res in result]
            self.assertEqual(ids, [822])
    def test_0305(self):
        with connection.cursor() as cursor:
            cursor.execute(answer_0305)
            result = cursor.fetchall()
            self.assertTrue(len(result) == 1)
            self.assertTrue(len(result[0]) == 2)
            self.assertEqual(result[0]["min_date"], "2020-01-01")
            self.assertEqual(result[0]["max_date"], "2023-12-31")
    def test_0306(self):
        with connection.cursor() as cursor:
            cursor.execute(answer_0306)
            result = cursor.fetchall()
            self.assertTrue(len(result) == 1)
            self.assertTrue(len(result[0]) == 2)
            self.assertEqual(result[0]["min_runtime"], 45)
            self.assertEqual(result[0]["max_runtime"], 238)
    def test_0307(self):
        with connection.cursor() as cursor:
            cursor.execute(answer_0307)
            result = cursor.fetchall()
            self.assertTrue(len(result) == 2)
            self.assertTrue(len(result[0]) == 2)
            titles = [res["title"] for res in result]
            self.assertEqual(titles, ["Gone with the Wind", "Sherlock Jr"])
    def test_0308(self):
        with connection.cursor() as cursor:
            cursor.execute(answer_0308)
            result = cursor.fetchall()
            self.assertTrue(len(result) == 2)
            self.assertTrue(len(result[0]) == 1)
            titles = [res["min_max_date"] for res in result]
            self.assertEqual(titles, ["2020-01-22", "2023-03-09"])
    def test_0309(self):
        with connection.cursor() as cursor:
            cursor.execute(answer_0309)
            result = cursor.fetchall()
            self.assertTrue(len(result) == 1143)
            self.assertTrue(len(result[0]) == 4)
            country_names = {res["country_name"] for res in result}
            self.assertEqual(country_names, {"Taiwan"})
    def test_0310(self):
        with connection.cursor() as cursor:
            cursor.execute(answer_0310)
            result = cursor.fetchall()
            self.assertTrue(len(result) == 97)
            self.assertTrue(len(result[0]) == 4)
            titles = {res["title"] for res in result}
            self.assertEqual(titles, {"Top Gun: Maverick"})
            names = [res["name"] for res in result]
            self.assertIn("Tom Cruise", names)
            self.assertIn("Val Kilmer", names)
            self.assertIn("Jennifer Connelly", names)

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
suite = unittest.TestLoader().loadTestsFromTestCase(TestQueryRecap)
runner = unittest.TextTestRunner(verbosity=2)
test_results = runner.run(suite)
number_of_failures = len(test_results.failures)
number_of_errors = len(test_results.errors)
number_of_test_runs = test_results.testsRun
number_of_successes = number_of_test_runs - (number_of_failures + number_of_errors)
chapter_index = 3
chapter_name = "快速複習基礎的 SQL 查詢敘述"
if number_of_successes == number_of_test_runs:
    print(f"恭喜您，通過「進階SQL的五十道練習」第{chapter_index}章：{chapter_name}全部{number_of_test_runs}個測試，你表現得非常好！")
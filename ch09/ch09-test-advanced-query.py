import unittest
import pymysql.cursors
import argparse

class TestAdvancedQuery(unittest.TestCase):
    def test_0901(self):
        with connection.cursor() as cursor:
            cursor.execute("""SELECT * FROM covid19.date_difference;""")
            number_of_columns = len(cursor.description)
            field_names = [i[0] for i in cursor.description]
            result = cursor.fetchall()
        self.assertTrue(number_of_columns == 2)
        number_of_rows = len(result)
        self.assertTrue(number_of_rows == 318)
        dates = [str(res["recorded_on"]) for res in result]
        self.assertEqual(dates[0], "2020-01-01")
        self.assertEqual(dates[-1], "2023-12-31")
    def test_0902(self):
        with connection.cursor() as cursor:
            cursor.execute("""SELECT * FROM tw_election_2020.presidential_votes_percentage;""")
            number_of_columns = len(cursor.description)
            field_names = [i[0] for i in cursor.description]
            result = cursor.fetchall()
        self.assertTrue(number_of_columns == 5)
        number_of_rows = len(result)
        self.assertTrue(number_of_rows == 3)
        total_votes = result[0]["total_votes"]
        self.assertEqual(str(total_votes), "14300940")
    def test_0903(self):
        with connection.cursor() as cursor:
            cursor.execute("""SELECT * FROM tw_election_2020.legislative_at_large_votes_percentage;""")
            number_of_columns = len(cursor.description)
            field_names = [i[0] for i in cursor.description]
            result = cursor.fetchall()
        self.assertTrue(number_of_columns == 4)
        number_of_rows = len(result)
        self.assertTrue(number_of_rows == 19)
        total_votes = result[0]["total_votes"]
        self.assertEqual(str(total_votes), "14160138")
    def test_0904(self):
        with connection.cursor() as cursor:
            cursor.execute("""SELECT * FROM covid19.most_populated_province;""")
            number_of_columns = len(cursor.description)
            field_names = [i[0] for i in cursor.description]
            result = cursor.fetchall()
        self.assertTrue(number_of_columns == 2)
        number_of_rows = len(result)
        self.assertTrue(number_of_rows == 30)
        countries = [res["country_name"] for res in result]
        provinces = [res["most_populated_province_name"] for res in result]
        self.assertIn("Australia", countries)
        self.assertIn("Canada", countries)
        self.assertIn("US", countries)
        self.assertIn("New South Wales", provinces)
        self.assertIn("Ontario", provinces)
        self.assertIn("California", provinces)
    def test_0905(self):
        with connection.cursor() as cursor:
            cursor.execute("""SELECT * FROM covid19.daily_cases;""")
            number_of_columns = len(cursor.description)
            field_names = [i[0] for i in cursor.description]
            result = cursor.fetchall()
        self.assertTrue(number_of_columns == 4)
        number_of_rows = len(result)
        self.assertTrue(number_of_rows == 328041)
        
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
suite = unittest.TestLoader().loadTestsFromTestCase(TestAdvancedQuery)
runner = unittest.TextTestRunner(verbosity=2)
test_results = runner.run(suite)
number_of_failures = len(test_results.failures)
number_of_errors = len(test_results.errors)
number_of_test_runs = test_results.testsRun
number_of_successes = number_of_test_runs - (number_of_failures + number_of_errors)
chapter_index = 9
chapter_name = "進階的 SQL 查詢"
if number_of_successes == number_of_test_runs:
    print(f"恭喜您，通過「進階SQL的五十道練習」第{chapter_index}章：{chapter_name}全部{number_of_test_runs}個測試，獲得進階查詢技巧之後，我們更有信心開始挑戰 LeetCode 網站上的 SQL 題目囉！")
import unittest
import pymysql.cursors
import argparse

class TestTCL(unittest.TestCase):
    def test_0701(self):
        conn = pymysql.connect(host='localhost',
                               user=f"{username}",
                               password=f"{user_password}",
                               db="transaction_control",
                               charset='utf8mb4',
                               cursorclass=pymysql.cursors.DictCursor)
    def test_0702(self):
        with connection.cursor() as cursor:
            cursor.execute("""SELECT * FROM transaction_control.accounts;""")
            number_of_columns = len(cursor.description)
            field_names = [i[0] for i in cursor.description]
        self.assertTrue(number_of_columns == 2)
        self.assertCountEqual(field_names, ["id", "balance"])
        with connection.cursor() as cursor:
            cursor.execute("""SELECT * FROM transaction_control.transfers;""")
            number_of_columns = len(cursor.description)
            field_names = [i[0] for i in cursor.description]
        self.assertTrue(number_of_columns == 4)
        self.assertCountEqual(field_names, ["id", "from_account_id", "to_account_id", "amount"])
    def test_0703(self):
        with connection.cursor() as cursor:
            cursor.execute("""SELECT * FROM transaction_control.accounts;""")
            result = cursor.fetchall()
        self.assertEqual(len(result), 2)
    def test_0704(self):
        with connection.cursor() as cursor:
            cursor.execute("""SELECT * FROM transaction_control.transfers;""")
            result = cursor.fetchall()
        amounts = [res["amount"] for res in result]
        self.assertEqual(amounts[0], 450)
        
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
suite = unittest.TestLoader().loadTestsFromTestCase(TestTCL)
runner = unittest.TextTestRunner(verbosity=2)
test_results = runner.run(suite)
number_of_failures = len(test_results.failures)
number_of_errors = len(test_results.errors)
number_of_test_runs = test_results.testsRun
number_of_successes = number_of_test_runs - (number_of_failures + number_of_errors)
chapter_index = 7
chapter_name = "交易控制語言"
if number_of_successes == number_of_test_runs:
    print(f"恭喜您，通過「進階SQL的五十道練習」第{chapter_index}章：{chapter_name}全部{number_of_test_runs}個測試，截至目前，我們總算認識了所有的 SQL 語言囉！")
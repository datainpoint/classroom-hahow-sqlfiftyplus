import unittest
import pymysql.cursors
import argparse

class TestDCL(unittest.TestCase):
    def test_0501(self):
        with connection.cursor() as cursor:
            cursor.execute("""SELECT User FROM mysql.user;""")
            result = cursor.fetchall()
        roles_and_users = [res["User"] for res in result]
        self.assertIn("administrator", roles_and_users)
        self.assertIn("normaluser", roles_and_users)
        self.assertIn("poweruser", roles_and_users)
    def test_0502(self):
        with connection.cursor() as cursor:
            cursor.execute("""SHOW GRANTS FOR 'administrator'@'localhost';""")
            result = cursor.fetchall()
        res = result[0]
        res_key = list(res.keys())[0]
        grant_str = ""
        for i in result:
            grant_s = i[res_key]
            grant_str += grant_s
        self.assertIn("ALL", grant_str.upper())
        with connection.cursor() as cursor:
            cursor.execute("""SHOW GRANTS FOR 'normaluser'@'localhost';""")
            result = cursor.fetchall()
        res = result[0]
        res_key = list(res.keys())[0]
        grant_str = ""
        for i in result:
            grant_s = i[res_key]
            grant_str += grant_s
        self.assertIn("SELECT", grant_str.upper())
        with connection.cursor() as cursor:
            cursor.execute("""SHOW GRANTS FOR 'poweruser'@'localhost';""")
            result = cursor.fetchall()
        res = result[0]
        res_key = list(res.keys())[0]
        grant_str = ""
        for i in result:
            grant_s = i[res_key]
            grant_str += grant_s
        self.assertIn("SELECT", grant_str.upper())
        self.assertIn("CREATE VIEW", grant_str.upper())
    def test_0503(self):
        connection = pymysql.connect(host='localhost',
                             user="ross",
                             password="geller",
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
        connection = pymysql.connect(host='localhost',
                             user="joey",
                             password="tribbiani",
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
        connection = pymysql.connect(host='localhost',
                             user="chandler",
                             password="bing",
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
        connection = pymysql.connect(host='localhost',
                             user=f"{username}",
                             password=f"{user_password}",
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
        with connection.cursor() as cursor:
            cursor.execute("""SHOW GRANTS FOR 'ross'@'localhost';""")
            result = cursor.fetchall()
        res = result[0]
        res_key = list(res.keys())[0]
        grant_str = ""
        for i in result:
            grant_s = i[res_key]
            grant_str += grant_s
        self.assertIn("administrator", grant_str.lower())
        with connection.cursor() as cursor:
            cursor.execute("""SHOW GRANTS FOR 'joey'@'localhost';""")
            result = cursor.fetchall()
        res = result[0]
        res_key = list(res.keys())[0]
        grant_str = ""
        for i in result:
            grant_s = i[res_key]
            grant_str += grant_s
        self.assertIn("normaluser", grant_str.lower())
        with connection.cursor() as cursor:
            cursor.execute("""SHOW GRANTS FOR 'chandler'@'localhost';""")
            result = cursor.fetchall()
        res = result[0]
        res_key = list(res.keys())[0]
        grant_str = ""
        for i in result:
            grant_s = i[res_key]
            grant_str += grant_s
        self.assertIn("poweruser", grant_str.lower())
        
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
suite = unittest.TestLoader().loadTestsFromTestCase(TestDCL)
runner = unittest.TextTestRunner(verbosity=2)
test_results = runner.run(suite)
number_of_failures = len(test_results.failures)
number_of_errors = len(test_results.errors)
number_of_test_runs = test_results.testsRun
number_of_successes = number_of_test_runs - (number_of_failures + number_of_errors)
chapter_index = 6
chapter_name = "資料控制語言"
if number_of_successes == number_of_test_runs:
    print(f"恭喜您，通過「進階SQL的五十道練習」第{chapter_index}章：{chapter_name}全部{number_of_test_runs}個測試，你的進度非常好，完課進度正式過半囉！")
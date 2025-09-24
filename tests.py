import unittest
from functions.get_files_info import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file


"""
class TestGetFilesInfo(unittest.TestCase):
    def test_1(self):
        result = get_files_info("calculator", ".")
        print("Result for current directory:")
        print(result)

    def test_2(self):
        result = get_files_info("calculator", "pkg")
        print("Result for 'pkg' directory:")
        print(result)

    def test_3(self):
        result = get_files_info("calculator", "/bin")
        print("Result for '/bin' directory:")
        print(result)

    def test_4(self):
        result = get_files_info("calculator", "../")
        print("Result for '../' directory:")
        print(result)
"""
"""
class TestGetFilesContent(unittest.TestCase):

    def test_1(self):
        result = get_file_content("calculator", ".")
        print("Result for current directory:")
        print(result)

    def test_2(self):
        result = get_file_content("calculator", "pkg")
        print("Result for 'pkg' directory:")
        print(result)

    def test_3(self):
        result = get_file_content("calculator", "/bin")
        print("Result for '/bin' directory:")
        print(result)

    def test_4(self):
        result = get_file_content("calculator", "../")
        print("Result for '../' directory:")
        print(result)

    def test_5(self):
        result = get_file_content("calculator", "lorem.txt")
        print("Result for 'lorem.txt' file:")
        print(result)

    def test_6(self):
        result = get_file_content("calculator", "main.py")
        print("Result for 'main.py' file:")
        print(result)

    def test_7(self):
        result = get_file_content("calculator", "pkg/calculator.py")
        print("Result for 'pkg/calculator.py' file:")
        print(result)

    def test_8(self):
        result = get_file_content("calculator", "/bin/cat")
        print("Result for '/bin/cat' file:")
        print(result)

    def test_9(self):
        result = get_file_content("calculator", "pkg/does_not_exist.py")
        print("Result for 'pkg/does_not_exist.py' file:")
        print(result)
"""

"""
class TestGetFilesInfo(unittest.TestCase):
    def test_1(self):
        result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
        print(result)

    def test_2(self):
        result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
        print(result)

    def test_3(self):
        result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
        print(result)
"""

class TestRunFile(unittest.TestCase):
    def test_1(self):
        result = run_python_file("calculator", "main.py")
        print("Result for 'main.py' file:")
        print(result)

    def test_2(self):
        result = run_python_file("calculator", "main.py", ["3 + 5"])
        print("Result for 'main.py' file:")
        print(result)

    def test_3(self):
        result = run_python_file("calculator", "tests.py")
        print("Result for 'tests.py' file:")
        print(result)

    def test_4(self):
        result = run_python_file("calculator", "../main.py")
        print("Result for '../main.py' file:")
        print(result)

    def test_5(self):
        result = run_python_file("calculator", "nonexistent.py")
        print("Result for 'nonexistent.py' file:")
        print(result)

if __name__ == "__main__":
    unittest.main()
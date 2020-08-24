import unittest

class TestCaseDemo(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("#" * 15)
        print("setUpClass: I will run only once before all tests")
        print("#" * 15)
    def setUp(self) -> None:
        print("setUp:I will run once before every test")

    def test_methodA(self):
        print("Running method A")

    def test_methodB(self):
        print("Running method B")

    def tearDown(self) -> None:
        print("tearDown:I will run after every test")
    @classmethod
    def tearDownClass(cls) -> None:
        print("#" * 15)
        print("tearDownClass: I will run only once after all tests")
        print("#" * 15)
if __name__ == '__main__':
    unittest.main(verbosity=2)
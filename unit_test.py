import unittest
from main import check_similar_level


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(check_similar_level(), 0.79)


if __name__ == '__main__':
    unittest.main()



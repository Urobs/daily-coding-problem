import unittest
from index import find_first_missing_integer

class TestResult(unittest.TestCase):
    def test_example_case(self):
        result_1 = find_first_missing_integer([3, 4, -1, 1])
        result_2 = find_first_missing_integer([1, 2, 0])
        self.assertEqual(result_1, 2)
        self.assertEqual(result_2, 3)

    def test_duplicated_num(self):
        result_1 = find_first_missing_integer([3, 3, 3, 4, 5, 7])
        result_2 = find_first_missing_integer([-1, -2, -2])
        self.assertEqual(result_1, 6)
        self.assertEqual(result_2, 0)

    def test_mutiple_missing(self):
        result = find_first_missing_integer([-3 , -1, 1, 3, 5, 7, 9])
        self.assertEqual(result, 2)    
if __name__ == '__main__':
    unittest.main()
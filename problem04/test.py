import unittest
from index import find_first_missing_integer, find_first_missing_integer_beta

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
        self.assertEqual(result_2, 1)

    def test_mutiple_missing(self):
        result = find_first_missing_integer([-3 , -1, 1, 3, 5, 7, 9])
        self.assertEqual(result, 2)

    def test_example_online(self):
        result_1 = find_first_missing_integer([2, 3, 7, 6, 8, -1, -10, 15])
        result_2 = find_first_missing_integer([2, 3, -7, 6, 8, 1, -10, 15])
        result_3 = find_first_missing_integer([1, 1, 0, -1, -2])
        self.assertEqual(result_1, 1)
        self.assertEqual(result_2, 4)
        self.assertEqual(result_3, 2)

    def test_beta_func(self):
        result_1 = find_first_missing_integer_beta([2, 3, 7, 6, 8, -1, -10, 15])
        result_2 = find_first_missing_integer_beta([2, 3, -7, 6, 8, 1, -10, 15])
        result_3 = find_first_missing_integer_beta([1, 1, 0, -1, -2])
        result_4 = find_first_missing_integer([-3 , -1, 1, 3, 5, 7, 9])
        result_5 = find_first_missing_integer([3, 4, -1, 1])
        result_6= find_first_missing_integer([1, 2, 0])
        self.assertEqual(result_1, 1)
        self.assertEqual(result_2, 4)
        self.assertEqual(result_3, 2)
        self.assertEqual(result_4, 2)
        self.assertEqual(result_5, 2)
        self.assertEqual(result_6, 3)

if __name__ == '__main__':
    unittest.main()
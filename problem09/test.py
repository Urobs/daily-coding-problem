import unittest
from index import count_non_ajacent_sum


class TestResult(unittest.TestCase):
    def test_example(self):
        num_list_1 = [2, 4, 6, 2, 5]
        num_list_2 = [1, 20, 3]
        num_list_3 = [5, 1, 1, 5]
        self.assertEqual(count_non_ajacent_sum(num_list_1), 13)
        self.assertEqual(count_non_ajacent_sum(num_list_2), 20)
        self.assertEqual(count_non_ajacent_sum(num_list_3), 10)

if __name__ == '__main__':
    unittest.main()
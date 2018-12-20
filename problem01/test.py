import unittest
import random

from index import find_out_if_sum_equal_k

class TestResult(unittest.TestCase):

    """
    test case
    """

    def test_blank_list(self):
        dist = []
        answer = find_out_if_sum_equal_k(dist, 100)
        self.assertFalse(answer)

    def test_example_case(self):
        dist = [10, 15, 3, 7]
        answer = find_out_if_sum_equal_k(dist, 17)
        self.assertTrue(answer)

    def test_one_element_case(self):
        dist = [20]
        answer = find_out_if_sum_equal_k(dist, 19)
        self.assertFalse(answer)

    def test_one_element_another_case(self):
        dist = [0]
        answer = find_out_if_sum_equal_k(dist, 0)
        self.assertFalse(answer)

    def test_big_length_list_case(self):
        source_list = list(range(0, 100))
        dist = random.sample(source_list, 10)
        print(dist)
        answer = find_out_if_sum_equal_k(dist, 40)
        print(answer)

if __name__ == '__main__':
    unittest.main()
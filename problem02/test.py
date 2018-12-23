import unittest

from index import product_expect_current_index_with_division, product_expect_current_index_without_division

class TestResult(unittest.TestCase):

    def test_example_case(self):
        l = [1, 2, 3, 4, 5]
        division_output = product_expect_current_index_with_division(l)
        without_div_output = product_expect_current_index_without_division(l)
        self.assertEqual([120, 60, 40, 30, 24], division_output)
        self.assertEqual([120, 60, 40, 30, 24], without_div_output)

    def test_edge_case(self):
        one_zero_case = [0, 1, 2, 3]
        two_zero_case = [1, 2, 3, 9, 0, 10, 30 ,50, 0]
        div_one_zero_output = product_expect_current_index_with_division(one_zero_case)
        div_two_zero_output = product_expect_current_index_with_division(two_zero_case)
        with_div_one_zero_output = product_expect_current_index_without_division(one_zero_case)
        with_div_two_zero_output = product_expect_current_index_without_division(two_zero_case)
        self.assertEqual([6, 0 , 0 ,0], div_one_zero_output)
        self.assertEqual([0, 0, 0, 0, 0, 0, 0, 0, 0], div_two_zero_output)
        self.assertEqual([6, 0 , 0 ,0], div_one_zero_output)
        self.assertEqual([0, 0, 0, 0, 0, 0, 0, 0, 0], div_two_zero_output)

if __name__ == '__main__':
    unittest.main()
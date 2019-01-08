import unittest
from index import count_unique_climb_ways

class TestResult(unittest.TestCase):
    def test_example_case(self):
        answer_1 = count_unique_climb_ways(4, [1, 2]) # 只测试了样本用例
        answer_2 = count_unique_climb_ways(4, [1, 2, 3])
        self.assertEqual(answer_1, 5)
        self.assertEqual(answer_2, 7)

if __name__ == '__main__':
    unittest.main()
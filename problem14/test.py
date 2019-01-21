from index import monte_carlo_estimate
import unittest

class TestResult(unittest.TestCase):
    def test_example(self):
        self.assertEqual(3.14, round(monte_carlo_estimate(10000000), 2))
if __name__ == '__main__':
    unittest.main()
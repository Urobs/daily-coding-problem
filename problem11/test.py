import unittest
from index import find_element_have

class TestResult(unittest.TestCase):
    def test_example_case(self):
        case_1 = ['dog', 'deer', 'deal']
        self.assertEqual(find_element_have('de', case_1), ['deer', 'deal'])

if __name__ == '__main__':
    unittest.main()
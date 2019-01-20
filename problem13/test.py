import unittest
from index import get_len_of_substr

class TestResult(unittest.TestCase):
    def test_example(self):
        self.assertEqual(get_len_of_substr(2, "abcba"), 3)
        self.assertEqual(get_len_of_substr(2, "aabbcc"), 4)
        self.assertEqual(get_len_of_substr(1, "aaaaaaa"), 7)
        self.assertEqual(get_len_of_substr(5, "afasfafadf"),10)

if __name__ == '__main__':
    unittest.main()
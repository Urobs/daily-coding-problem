import unittest
from index import count_decoded_ways  

class TestResult(unittest.TestCase):
    def test_example_case(self):
        string_case_1 = '123'
        string_case_2 = '1234'
        string_case_3 = '121'
        string_case_4 = '12321'
        string_case_5 = '1220'
        string_case_6 = '1230'
        decode_ways_case_1 = count_decoded_ways(string_case_1)
        decode_ways_case_2 = count_decoded_ways(string_case_2)
        decode_ways_case_3 = count_decoded_ways(string_case_3)
        decode_ways_case_4 = count_decoded_ways(string_case_4)
        decode_ways_case_5 = count_decoded_ways(string_case_5)
        decode_ways_case_6 = count_decoded_ways(string_case_6)
        self.assertEqual(decode_ways_case_1, 3)
        self.assertEqual(decode_ways_case_2, 3)
        self.assertEqual(decode_ways_case_3, 3)
        self.assertEqual(decode_ways_case_4, 6)
        self.assertEqual(decode_ways_case_5, 2)
        self.assertEqual(decode_ways_case_6, 0)

if __name__ == '__main__':
    unittest.main()
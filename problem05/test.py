import unittest
from index import car, cdr

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

class TestResult(unittest.TestCase):
    def test_example_case(self):
        self.assertEqual(car(cons(3, 4)), 3)
        self.assertEqual(cdr(cons(3, 4)), 4)

if __name__ == '__main__':
    unittest.main()
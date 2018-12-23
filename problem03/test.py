import unittest

from index import serialize, Node, deserialize

class TestResult(unittest.TestCase):
    def test_example_case(self):
        node = Node('root', Node('left', Node('left.left')), Node('right'))
        self.assertEqual(deserialize(serialize(node)).left.left.val, 'left.left')

if __name__ == '__main__':
    unittest.main()
import unittest
from index import Node, count_unival_tree

root_example = Node(0)
root_example.left = Node(1)
root_example.right = Node(0)
root_example.right.left = Node(1)
root_example.right.right = Node(0)
root_example.right.left.left = Node(1)
root_example.right.left.right = Node(1)
root_example.right.left.right.right = Node(1)
root_example.right.left.right.right.right = Node(1)
root_example.right.left.right.right.right.right = Node(1)
class TestResult(unittest.TestCase):
    def test_example_case(self):
        self.assertEqual(8, count_unival_tree(root_example))

if __name__ == '__main__':
    unittest.main()
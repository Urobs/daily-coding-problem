import unittest
from index import XORLinkedList, memory

class TestResult(unittest.TestCase):
    def test_method_add_and_get(self):
        xor_linked_list = XORLinkedList()
        xor_linked_list.add(1)
        xor_linked_list.add(2)
        xor_linked_list.add(3)
        xor_linked_list.add(5)
        for i in range(7, 15):
            xor_linked_list.add(i)
        get_node_index_3 = xor_linked_list.get(3)
        get_node_index_0 = xor_linked_list.get(0)
        get_node_index_1 = xor_linked_list.get(1)
        get_node_index_2 = xor_linked_list.get(2)
        for i in range(4, 12):
            self.assertEqual(xor_linked_list.get(i).element, i+3)
        self.assertEqual(get_node_index_0.element, 1)
        self.assertEqual(get_node_index_1.element, 2)
        self.assertEqual(get_node_index_2.element, 3)

if __name__ == '__main__':
        unittest.main()
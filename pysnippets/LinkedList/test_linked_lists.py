import unittest
from Circular_Linked_List import insert_end, delete_node, display
from Doubly_Linked_List import insert_end as insert_end_dll, delete_node as delete_node_dll, display as display_dll
from Singly_Linked_List import insert_end as insert_end_sll, delete_node as delete_node_sll, display as display_sll

class TestLinkedLists(unittest.TestCase):

    def test_circular_linked_list(self):
        head = None
        head = insert_end(head, 1)
        head = insert_end(head, 2)
        head = insert_end(head, 3)
        self.assertEqual(display(head), [1, 2, 3])
        head = delete_node(head, 2)
        self.assertEqual(display(head), [1, 3])

    def test_doubly_linked_list(self):
        head = None
        head = insert_end_dll(head, 1)
        head = insert_end_dll(head, 2)
        head = insert_end_dll(head, 3)
        self.assertEqual(display_dll(head), [1, 2, 3])
        head = delete_node_dll(head, 2)
        self.assertEqual(display_dll(head), [1, 3])

    def test_singly_linked_list(self):
        head = None
        head = insert_end_sll(head, 1)
        head = insert_end_sll(head, 2)
        head = insert_end_sll(head, 3)
        self.assertEqual(display_sll(head), [1, 2, 3])
        head = delete_node_sll(head, 2)
        self.assertEqual(display_sll(head), [1, 3])

if __name__ == '__main__':
    unittest.main() 
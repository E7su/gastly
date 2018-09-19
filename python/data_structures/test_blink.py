import unittest
import blink


class TestStringMethods(unittest.TestCase):

    def test_new_blink(self):
        blink_list = blink.BLinkedList()
        self.assertEqual(blink_list.head, None)
        self.assertEqual(blink_list.tail, None)
        self.assertEqual(blink_list.lenght, 0)

    def test_new_node(self):
        node = blink.Node()
        self.assertEqual(node.next, None)
        self.assertEqual(node.previous, None)
        self.assertEqual(node.value, None)

    def test_empty_if_empty(self):
        blink_list = blink.BLinkedList()
        self.assertEqual(blink_list.is_empty(), True)

    def test_empty_if_not_empty(self):
        blink_list = blink.BLinkedList()
        blink_list.head = 4
        blink_list.lenght = 1
        self.assertEqual(blink_list.is_empty(), False)
        self.assertEqual(blink_list.is_empty(), False)

    def test_add_node_to_empty(self):
        blink_list = blink.BLinkedList()
        node = blink.Node(3)
        blink_list.add_node_to_empty(node)
        self.assertEqual(blink_list.head.value, 3)
        self.assertEqual(blink_list.tail.value, 3)
        self.assertEqual(blink_list.head.previous, None)
        self.assertEqual(blink_list.tail.previous, None)
        self.assertEqual(blink_list.lenght, 1)

    def test_add_node_to_head_to_emtpy(self):
        blink_list = blink.BLinkedList()
        blink_list.add_node_to_head(42)
        self.assertEqual(blink_list.head.value, 42)
        self.assertEqual(blink_list.tail.value, 42)
        self.assertEqual(blink_list.head.previous, None)
        self.assertEqual(blink_list.tail.next, None)
        self.assertEqual(blink_list.lenght, 1)

    def test_add_node_to_head_to_not_emtpy(self):
        blink_list = blink.BLinkedList()
        blink_list.add_node_to_head(42)
        blink_list.add_node_to_head(4)
        self.assertEqual(blink_list.head.value, 4)
        self.assertEqual(blink_list.head.next.value, 42)
        self.assertEqual(blink_list.tail.previous.value, 4)
        self.assertEqual(blink_list.tail.value, 42)
        self.assertEqual(blink_list.head.previous, None)
        self.assertEqual(blink_list.tail.next, None)
        self.assertEqual(blink_list.lenght, 2)

    def test_add_node_to_tail_if_empty(self):
        blink_list = blink.BLinkedList()
        blink_list.add_node_to_tail(12)
        self.assertEqual(blink_list.head.value, 12)
        self.assertEqual(blink_list.tail.value, 12)
        self.assertEqual(blink_list.head.previous, None)
        self.assertEqual(blink_list.tail.next, None)
        self.assertEqual(blink_list.lenght, 1)

    def test_add_node_to_tail_if_not_empty(self):
        blink_list = blink.BLinkedList()
        blink_list.add_node_to_tail(17)
        blink_list.add_node_to_tail(12)
        self.assertEqual(blink_list.head.value, 17)
        self.assertEqual(blink_list.tail.value, 12)
        self.assertEqual(blink_list.head.previous, None)
        self.assertEqual(blink_list.tail.next, None)
        self.assertEqual(blink_list.lenght, 2)

    def test_add_node_to_first_position(self):
        blink_list = blink.BLinkedList()
        blink_list.add_node(value=1, pos=0)
        self.assertEqual(blink_list.head.value, 1)
        self.assertEqual(blink_list.tail.value, 1)
        self.assertEqual(blink_list.head.previous, None)
        self.assertEqual(blink_list.tail.next, None)
        self.assertEqual(blink_list.lenght, 1)

    def test_add_node_to_last_position(self):
        blink_list = blink.BLinkedList()
        blink_list.add_node(value=1, pos=0)
        blink_list.add_node(value=2, pos=1)
        blink_list.add_node(value=3, pos=2)
        self.assertEqual(blink_list.head.value, 1)
        self.assertEqual(blink_list.tail.value, 3)
        self.assertEqual(blink_list.head.previous, None)
        self.assertEqual(blink_list.tail.next, None)
        self.assertEqual(blink_list.lenght, 3)

    def test__get_node_by_position(self):
        blink_list = blink.BLinkedList()
        blink_list.add_node_to_tail(42)
        blink_list.add_node_to_tail(4)
        blink_list.add_node_to_tail(41)
        self.assertEqual(blink_list.head.value, 42)
        self.assertEqual(blink_list._get_node_by_position(0).value, 42)
        self.assertEqual(blink_list._get_node_by_position(1).value, 4)
        self.assertEqual(blink_list._get_node_by_position(2).value, 41)

    def test__add_node_to_current_node(self):
        blink_list = blink.BLinkedList()
        blink_list.add_node_to_tail(42)
        blink_list.add_node_to_tail(4)
        blink_list.add_node_to_tail(41)
        blink_list.add_node_to_tail(51)

        new_node = blink.Node(76)
        current_node = blink_list.head.next

        blink_list._add_node_to_current_node(new_node, current_node)
        self.assertEqual(blink_list.head.previous, None)
        self.assertEqual(blink_list.head.value, 42)
        self.assertEqual(blink_list.head.next.value, 76)
        self.assertEqual(blink_list.head.next.next.value, 4)
        self.assertEqual(blink_list.head.next.next.next.value, 41)
        self.assertEqual(blink_list.head.next.next.next.next.value, 51)

        self.assertEqual(blink_list.tail.next, None)
        self.assertEqual(blink_list.tail.value, 51)
        self.assertEqual(blink_list.tail.previous.value, 41)
        self.assertEqual(blink_list.tail.previous.previous.value, 4)
        self.assertEqual(blink_list.tail.previous.previous.previous.value, 76)
        self.assertEqual(
            blink_list.tail.previous.previous.previous.previous.value, 42)

        self.assertEqual(blink_list.lenght, 5)

    def test_add_node_to_position_after_tail(self):
        blink_list = blink.BLinkedList()
        blink_list.add_node(value=41, pos=0)
        blink_list.add_node(value=12, pos=1)
        blink_list.add_node(value=34, pos=2)
        self.assertEqual(blink_list.head.value, 41)
        self.assertEqual(blink_list.head.next.value, 12)
        self.assertEqual(blink_list.head.next.next.value, 34)
        self.assertEqual(blink_list.head.previous, None)
        self.assertEqual(blink_list.tail.value, 34)
        self.assertEqual(blink_list.tail.previous.value, 12)
        self.assertEqual(blink_list.tail.previous.previous.value, 41)
        self.assertEqual(blink_list.tail.next, None)
        self.assertEqual(blink_list.lenght, 3)

    def test_change_node_with_head(self):
        blink_list = blink.BLinkedList()
        blink_list.add_node(value=41, pos=0)
        blink_list.add_node(value=42, pos=0)
        self.assertEqual(blink_list.head.value, 42)
        self.assertEqual(blink_list.head.next.value, 41)
        self.assertEqual(blink_list.head.previous, None)
        self.assertEqual(blink_list.tail.value, 41)
        self.assertEqual(blink_list.tail.previous.value, 42)
        self.assertEqual(blink_list.tail.next, None)
        self.assertEqual(blink_list.lenght, 2)

    def test_add_node_to_wrong_position(self):
        blink_list = blink.BLinkedList()
        blink_list.add_node(value=451, pos=0)
        blink_list.add_node(value=1, pos=1)
        blink_list.add_node(value=84, pos=2)
        blink_list.add_node(value=7, pos=1)
        self.assertEqual(blink_list.head.value, 451)
        self.assertEqual(blink_list.head.next.value, 7)
        self.assertEqual(blink_list.head.next.next.value, 1)
        self.assertEqual(blink_list.head.next.next.next.value, 84)
        self.assertEqual(blink_list.head.previous, None)
        self.assertEqual(blink_list.tail.value, 84)
        self.assertEqual(blink_list.tail.previous.value, 1)
        self.assertEqual(blink_list.tail.previous.previous.value, 7)
        self.assertEqual(blink_list.tail.previous.previous.previous.value, 451)
        self.assertEqual(blink_list.tail.next, None)
        self.assertEqual(blink_list.lenght, 4)

    def test_add_node_to_wrong_position(self):
        blink_list = blink.BLinkedList()
        blink_list.add_node(value=7, pos=0)
        with self.assertRaises(blink.BLinkedListIndexException):
            blink_list.add_node(value=42, pos=5)
        with self.assertRaises(blink.BLinkedListIndexException):
            blink_list.add_node(value=42, pos=172)

    def test_delete_node_from_head(self):
        blink_list = blink.BLinkedList()
        blink_list.add_node_to_head(value=1214)
        blink_list.add_node_to_head(value=73)
        blink_list.add_node_to_head(value=790)
        blink_list.add_node_to_head(value=4)
        blink_list.delete_node_from_head()
        self.assertEqual(blink_list.head.value, 790)
        self.assertEqual(blink_list.head.next.value, 73)
        self.assertEqual(blink_list.head.next.next.value, 1214)
        self.assertEqual(blink_list.head.previous, None)
        self.assertEqual(blink_list.tail.value, 1214)
        self.assertEqual(blink_list.tail.previous.value, 73)
        self.assertEqual(blink_list.tail.previous.previous.value, 790)
        self.assertEqual(blink_list.tail.next, None)
        self.assertEqual(blink_list.lenght, 3)

    def test_delete_node_from_head_in_empty_list(self):
        blink_list = blink.BLinkedList()
        with self.assertRaises(blink.BLinkedListIndexException):
            blink_list.delete_node_from_head()
        self.assertEqual(blink_list.lenght, 0)
        self.assertEqual(blink_list.head, None)
        self.assertEqual(blink_list.tail, None)

    def test_delete_node_from_tail(self):
        blink_list = blink.BLinkedList()
        blink_list.add_node_to_head(value=1214)
        blink_list.add_node_to_head(value=73)
        blink_list.add_node_to_head(value=790)
        blink_list.add_node_to_head(value=4)
        blink_list.delete_node_from_tail()
        self.assertEqual(blink_list.head.value, 4)
        self.assertEqual(blink_list.head.next.value, 790)
        self.assertEqual(blink_list.head.next.next.value, 73)
        self.assertEqual(blink_list.head.previous, None)
        self.assertEqual(blink_list.tail.value, 73)
        self.assertEqual(blink_list.tail.previous.value, 790)
        self.assertEqual(blink_list.tail.previous.previous.value, 4)
        self.assertEqual(blink_list.tail.next, None)
        self.assertEqual(blink_list.lenght, 3)

    def test_delete_node_from_tail_in_empty_list(self):
        blink_list = blink.BLinkedList()
        with self.assertRaises(blink.BLinkedListIndexException):
            blink_list.delete_node_from_tail()
        self.assertEqual(blink_list.lenght, 0)
        self.assertEqual(blink_list.head, None)
        self.assertEqual(blink_list.tail, None)

    def test_delete_node_from_position(self):
        blink_list = blink.BLinkedList()
        blink_list.add_node_to_head(value=1214)
        blink_list.add_node_to_head(value=73)
        blink_list.add_node_to_head(value=790)
        blink_list.add_node_to_head(value=4)
        blink_list.delete_node_from_position(2)
        self.assertEqual(blink_list.head.value, 4)
        self.assertEqual(blink_list.head.next.value, 790)
        self.assertEqual(blink_list.head.next.next.value, 1214)
        self.assertEqual(blink_list.head.previous, None)
        self.assertEqual(blink_list.tail.value, 1214)
        self.assertEqual(blink_list.tail.previous.value, 790)
        self.assertEqual(blink_list.tail.previous.previous.value, 4)
        self.assertEqual(blink_list.tail.next, None)
        self.assertEqual(blink_list.lenght, 3)

    def test_delete_node_from_first_position(self):
        blink_list = blink.BLinkedList()
        blink_list.add_node_to_head(value=1214)
        blink_list.add_node_to_head(value=73)
        blink_list.add_node_to_head(value=790)
        blink_list.add_node_to_head(value=4)
        blink_list.delete_node_from_position(0)
        self.assertEqual(blink_list.head.value, 790)
        self.assertEqual(blink_list.head.next.value, 73)
        self.assertEqual(blink_list.head.next.next.value, 1214)
        self.assertEqual(blink_list.head.previous, None)
        self.assertEqual(blink_list.tail.value, 1214)
        self.assertEqual(blink_list.tail.previous.value, 73)
        self.assertEqual(blink_list.tail.previous.previous.value, 790)
        self.assertEqual(blink_list.tail.next, None)
        self.assertEqual(blink_list.lenght, 3)

    def test_delete_node_from_last_position(self):
        blink_list = blink.BLinkedList()
        blink_list.add_node_to_head(value=1214)
        blink_list.add_node_to_head(value=73)
        blink_list.add_node_to_head(value=790)
        blink_list.add_node_to_head(value=4)
        blink_list.delete_node_from_position(3)
        self.assertEqual(blink_list.head.value, 4)
        self.assertEqual(blink_list.head.next.value, 790)
        self.assertEqual(blink_list.head.next.next.value, 73)
        self.assertEqual(blink_list.head.previous, None)
        self.assertEqual(blink_list.tail.value, 73)
        self.assertEqual(blink_list.tail.previous.value, 790)
        self.assertEqual(blink_list.tail.previous.previous.value, 4)
        self.assertEqual(blink_list.tail.next, None)
        self.assertEqual(blink_list.lenght, 3)

    if __name__ == '__main__':
        unittest.main()

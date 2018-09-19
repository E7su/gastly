import unittest
import bqueue as bq


class TestBLinkedQueue(unittest.TestCase):

    def test_new_blinked_queue(self):
        bqueue = bq.BLinkedQueue()
        self.assertEqual(bqueue.is_empty(), True)
        self.assertEqual(bqueue.blink.lenght, 0)
        self.assertEqual(bqueue.blink.head, None)
        self.assertEqual(bqueue.blink.tail, None)

    def test_empty_if_empty(self):
        bqueue = bq.BLinkedQueue()
        self.assertEqual(bqueue.is_empty(), True)

    def test_empty_if_not_empty(self):
        bqueue = bq.BLinkedQueue()
        bqueue.blink.head = 4
        self.assertEqual(bqueue.is_empty(), False)

    def test_put_first_element_to_blinked_queue(self):
        bqueue = bq.BLinkedQueue()
        bqueue.put(4)
        self.assertEqual(bqueue.is_empty(), False)
        self.assertEqual(bqueue.blink.head.value, 4)
        self.assertEqual(bqueue.blink.tail.value, 4)
        self.assertEqual(bqueue.blink.head.previous, None)
        self.assertEqual(bqueue.blink.tail.previous, None)
        self.assertEqual(bqueue.blink.lenght, 1)

    def test_put_three_elements_to_blinked_queue(self):
        bqueue = bq.BLinkedQueue()
        bqueue.put(-42)
        bqueue.put(0)
        bqueue.put(16)
        self.assertEqual(bqueue.is_empty(), False)
        self.assertEqual(bqueue.blink.head.value, -42)
        self.assertEqual(bqueue.blink.head.next.value, 0)
        self.assertEqual(bqueue.blink.head.next.next.value, 16)
        self.assertEqual(bqueue.blink.head.next.next.next, None)
        self.assertEqual(bqueue.blink.tail.value, 16)
        self.assertEqual(bqueue.blink.tail.previous.value, 0)
        self.assertEqual(bqueue.blink.tail.previous.previous.value, -42)
        self.assertEqual(bqueue.blink.tail.previous.previous.previous, None)
        self.assertEqual(bqueue.blink.head.previous, None)
        self.assertEqual(bqueue.blink.tail.next, None)
        self.assertEqual(bqueue.blink.lenght, 3)

    def test_pop_element_from_blinked_queue(self):
        bqueue = bq.BLinkedQueue()
        bqueue.put(126)
        bqueue.put(5555)
        bqueue.put(-176)
        self.assertEqual(bqueue.is_empty(), False)
        self.assertEqual(bqueue.blink.head.value, 126)
        self.assertEqual(bqueue.blink.head.next.value, 5555)
        self.assertEqual(bqueue.blink.head.next.next.value, -176)
        self.assertEqual(bqueue.blink.tail.value, -176)
        self.assertEqual(bqueue.blink.tail.previous.value, 5555)
        self.assertEqual(bqueue.blink.tail.previous.previous.value, 126)
        self.assertEqual(bqueue.blink.head.previous, None)
        self.assertEqual(bqueue.blink.tail.next, None)
        self.assertEqual(bqueue.blink.lenght, 3)

        bqueue.pop()
        self.assertEqual(bqueue.is_empty(), False)
        self.assertEqual(bqueue.blink.head.value, 5555)
        self.assertEqual(bqueue.blink.head.next.value, -176)
        self.assertEqual(bqueue.blink.head.next.next, None)
        self.assertEqual(bqueue.blink.tail.value, -176)
        self.assertEqual(bqueue.blink.tail.previous.value, 5555)
        self.assertEqual(bqueue.blink.tail.previous.previous, None)
        self.assertEqual(bqueue.blink.head.previous, None)
        self.assertEqual(bqueue.blink.tail.next, None)
        self.assertEqual(bqueue.blink.lenght, 2)

    def test_pop_all_elements_from_blinked_queue(self):
        bqueue = bq.BLinkedQueue()
        bqueue.put(142)
        bqueue.put(5)
        bqueue.put(-16)
        self.assertEqual(bqueue.is_empty(), False)
        self.assertEqual(bqueue.blink.head.value, 142)
        self.assertEqual(bqueue.blink.head.next.value, 5)
        self.assertEqual(bqueue.blink.head.next.next.value, -16)
        self.assertEqual(bqueue.blink.tail.value, -16)
        self.assertEqual(bqueue.blink.tail.previous.value, 5)
        self.assertEqual(bqueue.blink.tail.previous.previous.value, 142)
        self.assertEqual(bqueue.blink.head.previous, None)
        self.assertEqual(bqueue.blink.tail.next, None)
        self.assertEqual(bqueue.blink.lenght, 3)

        node = bqueue.pop()
        self.assertEqual(node.value, 142)
        self.assertEqual(bqueue.is_empty(), False)
        self.assertEqual(bqueue.blink.head.value, 5)
        self.assertEqual(bqueue.blink.head.next.value, -16)
        self.assertEqual(bqueue.blink.head.next.next, None)
        self.assertEqual(bqueue.blink.tail.value, -16)
        self.assertEqual(bqueue.blink.tail.previous.value, 5)
        self.assertEqual(bqueue.blink.tail.previous.previous, None)
        self.assertEqual(bqueue.blink.head.previous, None)
        self.assertEqual(bqueue.blink.tail.next, None)
        self.assertEqual(bqueue.blink.lenght, 2)

        node = bqueue.pop()
        self.assertEqual(node.value, 5)
        self.assertEqual(bqueue.is_empty(), False)
        self.assertEqual(bqueue.blink.head.value, -16)
        self.assertEqual(bqueue.blink.head.next, None)
        self.assertEqual(bqueue.blink.tail.value, -16)
        self.assertEqual(bqueue.blink.tail.previous, None)
        self.assertEqual(bqueue.blink.head.previous, None)
        self.assertEqual(bqueue.blink.tail.next, None)
        self.assertEqual(bqueue.blink.lenght, 1)

        node = bqueue.pop()
        self.assertEqual(node.value, -16)
        self.assertEqual(bqueue.is_empty(), True)
        self.assertEqual(bqueue.blink.head, None)
        self.assertEqual(bqueue.blink.tail, None)
        self.assertEqual(bqueue.blink.lenght, 0)

    def test_len(self):
        bqueue = bq.BLinkedQueue()
        self.assertEqual(len(bqueue), 0)
        bqueue.put(-42)
        self.assertEqual(len(bqueue), 1)
        bqueue.put(0)
        self.assertEqual(len(bqueue), 2)
        bqueue.put(16)
        self.assertEqual(len(bqueue), 3)
        bqueue.pop()
        self.assertEqual(len(bqueue), 2)

    def test_top_for_blinked_queue(self):
        bqueue = bq.BLinkedQueue()
        bqueue.blink.head = 1412
        self.assertEqual(bqueue.top(), 1412)
        bqueue.blink.head = -2
        self.assertEqual(bqueue.top(), -2)
        bqueue.blink.head = 0
        self.assertEqual(bqueue.top(), 0)

    def test_tayl_for_blinked_queue(self):
        bqueue = bq.BLinkedQueue()
        bqueue.blink.tail = 1412
        self.assertEqual(bqueue.tail(), 1412)
        bqueue.blink.tail = -2
        self.assertEqual(bqueue.tail(), -2)
        bqueue.blink.tail = 0
        self.assertEqual(bqueue.tail(), 0)

    def test_get_value(self):
        bqueue = bq.BLinkedQueue()
        bqueue.put(4)
        node = bqueue.blink.tail
        self.assertEqual(bqueue.get_value(node), 4)

        bqueue.put(65536)
        node = bqueue.blink.tail
        self.assertEqual(bqueue.get_value(node), 65536)

        bqueue.put(-923)
        node = bqueue.blink.tail
        self.assertEqual(bqueue.get_value(node), -923)

        bqueue.put(0)
        node = bqueue.blink.tail
        self.assertEqual(bqueue.get_value(node), 0)


if __name__ == '__main__':
    unittest.main()

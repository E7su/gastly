# -*- coding: utf-8 -*-
import unittest
import mqueue as mq


class TestSuperMassiveCircleQueue(unittest.TestCase):

    def test_new_default_massive_queue(self):
        mqueue = mq.SuperMassiveCircleQueue()
        self.assertEqual(mqueue.is_empty(), True)
        self.assertEqual(mqueue.lenght, 0)
        self.assertEqual(len(mqueue.massive), 20)
        self.assertEqual(mqueue.massive, [None] * 20)
        self.assertEqual(mqueue.head, -1)
        self.assertEqual(mqueue.tail, -1)

    def test_new_massive_queue_with_capacity(self, capacity=15):
        mqueue = mq.SuperMassiveCircleQueue(capacity)
        self.assertEqual(mqueue.is_empty(), True)
        self.assertEqual(mqueue.lenght, 0)
        self.assertEqual(len(mqueue.massive), capacity)
        self.assertEqual(mqueue.massive, [None] * capacity)
        self.assertEqual(mqueue.head, -1)
        self.assertEqual(mqueue.tail, -1)

    def test_new_massive_queue_with_null_capacity(self, capacity=0):
        mqueue = mq.SuperMassiveCircleQueue(capacity)
        self.assertEqual(mqueue.is_empty(), True)
        self.assertEqual(mqueue.lenght, 0)
        self.assertEqual(len(mqueue.massive), capacity)
        self.assertEqual(mqueue.massive, [])
        self.assertEqual(mqueue.head, -1)
        self.assertEqual(mqueue.tail, -1)

    def test_new_massive_queue_with_negative_capacity(self, capacity=-10):
        mqueue = mq.SuperMassiveCircleQueue(capacity)
        self.assertEqual(mqueue.is_empty(), True)
        self.assertEqual(mqueue.lenght, 0)
        self.assertEqual(len(mqueue.massive), 0)
        self.assertEqual(mqueue.massive, [])
        self.assertEqual(mqueue.head, -1)
        self.assertEqual(mqueue.tail, -1)

    def test_is_empty_if_empty(self):
        mqueue = mq.SuperMassiveCircleQueue()
        mqueue.lenght = 0
        self.assertEqual(mqueue.is_empty(), True)

    def test_is_empty_if_not_empty(self):
        mqueue = mq.SuperMassiveCircleQueue()
        mqueue.lenght = 12
        self.assertEqual(mqueue.is_empty(), False)

    def test_is_full_if_empty(self):
        mqueue = mq.SuperMassiveCircleQueue()
        mqueue.lenght = 0
        mqueue.capacity = 0
        self.assertEqual(mqueue.is_full(), True)

    def test_is_full_if_full_and_not_empty(self):
        mqueue = mq.SuperMassiveCircleQueue()
        mqueue.lenght = 12
        mqueue.capacity = 12
        self.assertEqual(mqueue.is_full(), True)

    def test_is_full_if_not_full_and_not_empty(self):
        mqueue = mq.SuperMassiveCircleQueue()
        mqueue.lenght = 7
        mqueue.capacity = 10
        self.assertEqual(mqueue.is_full(), False)

    def test_is_full_if_full_and_not_empty(self):
        mqueue = mq.SuperMassiveCircleQueue()
        mqueue.lenght = 8
        mqueue.capacity = 8
        self.assertEqual(mqueue.is_full(), True)

    def test_len(self):
        mqueue = mq.SuperMassiveCircleQueue()
        mqueue.lenght = 12
        self.assertEqual(len(mqueue), 12)

    def test_len_if_empty(self):
        mqueue = mq.SuperMassiveCircleQueue()
        mqueue.lenght = 0
        self.assertEqual(len(mqueue), 0)

    def test_len_if_negativa_lenght(self):
        mqueue = mq.SuperMassiveCircleQueue()
        mqueue.lenght = -1
        with self.assertRaises(ValueError):
            len(mqueue)
        mqueue.lenght = -100500
        with self.assertRaises(ValueError):
            len(mqueue)

    def test_print_fullness(self):
        mqueue = mq.SuperMassiveCircleQueue(capacity=15)
        mqueue.lenght = 12
        mqueue.massive = [None] * 15
        full = mqueue.print_fullness()
        self.assertEqual(full, '12/15')

        mqueue = mq.SuperMassiveCircleQueue(capacity=10)
        mqueue.lenght = 0
        mqueue.massive = [None] * 10
        full = mqueue.print_fullness()
        self.assertEqual(full, '0/10')

    def test_print_fullness_on_empty_massive(self):
        mqueue = mq.SuperMassiveCircleQueue(capacity=0)
        mqueue.lenght = 0
        full = mqueue.print_fullness()
        self.assertEqual(full, '0/0')

    def test_print_fullness_on_massive_with_negative_lenght(self):
        mqueue = mq.SuperMassiveCircleQueue(capacity=10)
        mqueue.lenght = -1
        with self.assertRaises(ValueError):
            mqueue.print_fullness()

    def test__put_first_node_to_massive_queue(self):
        mqueue = mq.SuperMassiveCircleQueue()
        mqueue.put(4)
        self.assertEqual(mqueue.is_empty(), False)

        head = mqueue.head
        self.assertEqual(head, 0)
        self.assertEqual(mqueue.massive[head], 4)

        tail = mqueue.tail
        self.assertEqual(tail, 0)
        self.assertEqual(mqueue.massive[tail], 4)
        self.assertEqual(mqueue.lenght, 1)

    def test__put_negative_first_node_to_massive_queue(self):
        mqueue = mq.SuperMassiveCircleQueue()
        mqueue.put(-42)
        self.assertEqual(mqueue.is_empty(), False)

        head = mqueue.head
        self.assertEqual(head, 0)
        self.assertEqual(mqueue.massive[head], -42)

        tail = mqueue.tail
        self.assertEqual(tail, 0)
        self.assertEqual(mqueue.massive[tail], -42)
        self.assertEqual(mqueue.lenght, 1)

    def test_put_three_nodes_to_massive_queue(self):
        mqueue = mq.SuperMassiveCircleQueue(3)
        mqueue.put(4)
        self.assertEqual(mqueue.is_empty(), False)
        self.assertEqual(mqueue.lenght, 1)
        head = mqueue.head
        self.assertEqual(head, 0)
        self.assertEqual(mqueue.massive[head], 4)
        tail = mqueue.tail
        self.assertEqual(tail, 0)
        self.assertEqual(mqueue.massive[tail], 4)

        mqueue.put(-7)
        self.assertEqual(mqueue.is_empty(), False)
        self.assertEqual(mqueue.lenght, 2)
        head = mqueue.head
        self.assertEqual(head, 0)
        self.assertEqual(mqueue.massive[head], 4)
        tail = mqueue.tail
        self.assertEqual(tail, 1)
        self.assertEqual(mqueue.massive[tail], -7)

        mqueue.put(0)
        self.assertEqual(mqueue.is_empty(), False)
        self.assertEqual(mqueue.lenght, 3)
        head = mqueue.head
        self.assertEqual(head, 0)
        self.assertEqual(mqueue.massive[head], 4)
        tail = mqueue.tail
        self.assertEqual(tail, 2)
        self.assertEqual(mqueue.massive[tail], 0)

    def test_put_node_if_full_queue(self):
        mqueue = mq.SuperMassiveCircleQueue(3)
        mqueue.lenght = 3
        mqueue.head = 0
        mqueue.tail = 2
        mqueue.massive = [-213, 0, 42]
        with self.assertRaises(IndexError):
            mqueue.put(8)

    def test_put_node_if_tail_is_last(self):
        mqueue = mq.SuperMassiveCircleQueue(3)
        mqueue.lenght = 2
        mqueue.head = 1
        mqueue.tail = 2
        mqueue.massive = [-213, 0, 42]
        mqueue.put(120)
        self.assertEqual(mqueue.head, 1)
        self.assertEqual(mqueue.massive[mqueue.head], 0)
        self.assertEqual(mqueue.tail, 0)
        self.assertEqual(mqueue.massive[mqueue.tail], 120)

    def test_put_node_if_head_is_null(self):
        mqueue = mq.SuperMassiveCircleQueue(3)
        mqueue.lenght = 2
        mqueue.head = 0
        mqueue.tail = 1
        mqueue.massive = [17, 16, 42]
        mqueue.put(5)
        self.assertEqual(mqueue.head, 0)
        self.assertEqual(mqueue.massive[mqueue.head], 17)
        self.assertEqual(mqueue.tail, 2)
        self.assertEqual(mqueue.massive[mqueue.tail], 5)

    def test_put_node_if_circle_is_full(self):
        mqueue = mq.SuperMassiveCircleQueue(3)
        mqueue.massive = [9, 5, 4]
        mqueue.lenght = 3
        mqueue.tail = 0
        mqueue.head = 1
        with self.assertRaises(IndexError):
            mqueue.put(8)

    def test_put_node_if_head_more_than_tail(self):
        mqueue = mq.SuperMassiveCircleQueue(3)
        mqueue.lenght = 2
        mqueue.head = 3
        mqueue.tail = 1
        mqueue.massive = [32, 0, 242, -43]
        mqueue.put(123)
        self.assertEqual(mqueue.head, 3)
        self.assertEqual(mqueue.massive[mqueue.head], -43)
        self.assertEqual(mqueue.tail, 2)
        self.assertEqual(mqueue.massive[mqueue.tail], 123)

    def test_take_if_empty(self):
        mqueue = mq.SuperMassiveCircleQueue()
        with self.assertRaises(IndexError):
            mqueue.take()

    def test_take_three_nodes_from_massive_queue(self):
        mqueue = mq.SuperMassiveCircleQueue()
        mqueue.massive = [76, 0, -12]
        mqueue.lenght = 3
        mqueue.head = 0
        mqueue.tail = 2
        task = mqueue.take()
        self.assertEqual(task, 76)
        self.assertEqual(mqueue.lenght, 2)
        self.assertEqual(mqueue.head, 1)
        self.assertEqual(mqueue.massive[mqueue.head], 0)
        self.assertEqual(mqueue.tail, 2)
        self.assertEqual(mqueue.massive[mqueue.tail], -12)

        task = mqueue.take()
        self.assertEqual(task, 0)
        self.assertEqual(mqueue.head, 2)
        self.assertEqual(mqueue.massive[mqueue.head], -12)
        self.assertEqual(mqueue.tail, 2)
        self.assertEqual(mqueue.massive[mqueue.tail], -12)

    def test_take_more_then_last(self):
        mqueue = mq.SuperMassiveCircleQueue()
        mqueue.massive = [1, 2]
        mqueue.lenght = 2
        mqueue.take()
        mqueue.take()
        with self.assertRaises(IndexError):
            mqueue.take()

    def test_get_top_value_for_massive_queue(self):
        mqueue = mq.SuperMassiveCircleQueue()
        mqueue.massive = [1412, -2, 0]
        mqueue.head = 0
        self.assertEqual(mqueue.get_top_value(), 1412)

        mqueue.head = 1
        self.assertEqual(mqueue.get_top_value(), -2)

        mqueue.head = 2
        self.assertEqual(mqueue.get_top_value(), 0)

        mqueue.head = 2
        mqueue.massive = [-71, 0, -7]
        self.assertEqual(mqueue.get_top_value(), -7)

        mqueue.head = 0
        mqueue.massive = [0]
        self.assertEqual(mqueue.get_top_value(), 0)

    def test_get_tail_value_for_massive_queue(self):
        mqueue = mq.SuperMassiveCircleQueue()
        mqueue.massive = [1412, -2, 0]
        mqueue.head = 0
        mqueue.tail = 2
        self.assertEqual(mqueue.get_tail_value(), 0)

        mqueue.massive = [-2, 1230, 12313]
        mqueue.tail = 1
        self.assertEqual(mqueue.get_tail_value(), 1230)

        mqueue.massive = [0]
        mqueue.tail = 0
        self.assertEqual(mqueue.get_tail_value(), 0)

        mqueue.massive = [5, 7, 90]
        mqueue.tail = 0
        self.assertEqual(mqueue.get_tail_value(), 5)


if __name__ == '__main__':
    unittest.main()

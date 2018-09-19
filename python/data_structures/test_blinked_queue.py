import unittest
import bqueue as bq


class TestBLinkedQueue(unittest.TestCase):

    def test_new_blinked_queu(self):
        bqueue = bq.BLinkedQueue()
        self.assertEqual(bqueue.is_empty(), True)
        self.assertEqual(bqueue.blink.lenght, 0)
        self.assertEqual(bqueue.blink.head, None)
        self.assertEqual(bqueue.blink.tail, None)


if __name__ == '__main__':
    unittest.main()

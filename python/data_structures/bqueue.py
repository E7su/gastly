from blink import BLinkedList


class BLinkedQueue(object):
    def __init__(self):
        self.blink = BLinkedList()

    def __len__(self):
        return self.blink.lenght

    def put(self, value):
        self.blink.add_node_to_tail(value)

    def pop(self):
        task = self.blink.head
        self.blink.delete_node_from_head()
        return task

    def is_empty(self):
        return self.blink.is_empty()

    def top(self):
        return self.blink.head

    def tail(self):
        return self.blink.tail

    @staticmethod
    def get_value(node):
        return node.value

    def pprint(self):
        return self.blink.pprint()


def main():
    blinked_queue = BLinkedQueue()
    print('>>> Is empty: ', blinked_queue.is_empty())
    print('>>> Top: ', blinked_queue.top())
    print()

    blinked_queue.put(4)
    top = blinked_queue.top()
    blinked_queue.pprint()
    print('>>> Top: ', top)
    print('>>> Tail: ', top)
    print()

    blinked_queue.put(7)
    top = blinked_queue.top()
    blinked_queue.pprint()
    print('>>> Top: ', top)
    tail = blinked_queue.tail()
    print('>>> Tail: ', tail)
    print()

    blinked_queue.pop()
    blinked_queue.pprint()
    print()


if __name__ == '__main__':
    main()

class BLinkedListIndexException(Exception):
    def __init__(self, message):
        Exception.__init__(self, message)


class Node(object):
    def __init__(self, value=None, next=None, previous=None):
        self.value = value
        self.next = next
        self.previous = previous


class BLinkedList(object):
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
        self.lenght = 0

    def is_empty(self):
        return self.head is None

    def add_node_to_empty(self, node):
        self.head = node
        self.tail = node
        self.tail.next = None
        self.head.previous = None
        self.lenght += 1

    def add_node_to_head(self, value):
        node = Node(value)
        if self.is_empty():
            self.add_node_to_empty(node)
        else:
            self.head.previous = node
            node.next = self.head
            self.head = node
            node.previous = None
            self.lenght += 1

    def add_node_to_tail(self, value):
        node = Node(value)
        if self.is_empty():
            self.add_node_to_empty(node)
        else:
            node.previous = self.tail
            node.next = None
            self.tail.next = node
            self.tail = node
            self.lenght += 1

    def add_node(self, value, pos):
        if pos == 0:
            self.add_node_to_head(value)
        elif pos == self.lenght:
            self.add_node_to_tail(value)
        elif pos < self.lenght:
            current_node = self._get_node_by_position(pos)
            print(current_node.value)
            node = Node(value)
            self._add_node_to_current_node(node, current_node)
        else:
            minimum_nodes = pos - self.lenght + 1
            message = ("Trying to add node to position {0} "
                       "to list with lenght {1}. \n"
                       "List numeration starts with number 0.\n"
                       "Please, add at least {2} nodes "
                       "before adding new node "
                       "to position {0}.").format(pos,
                                                  self.lenght,
                                                  minimum_nodes)
            raise BLinkedListIndexException(message)

    def _get_node_by_position(self, pos):
        current_node = self.head
        if pos == 0:
            return current_node
        for i in range(1, self.lenght):
            current_node = current_node.next
            if i == pos:
                return current_node

    def _add_node_to_current_node(self, new_node, current_node):
        new_node.next = current_node
        new_node.previous = current_node.previous
        current_node.previous.next = new_node
        current_node.previous = new_node
        self.lenght += 1

    def delete_node_from_head(self):
        if self.head is None:
            message = "Trying to delete node from head "
            "of empty list. \n"
            "Please, add at least 1 node "
            "before use this operation."
            raise BLinkedListIndexException(message)
        else:
            self.head = self.head.next
            self.head.previous = None
            self.lenght -= 1

    def delete_node_from_tail(self):
        if self.head is None:
            message = "Trying to delete node from tail "
            "of empty list. \n"
            "Please, add at least 1 node "
            "before use this operation."
            raise BLinkedListIndexException(message)
        else:
            self.tail = self.tail.previous
            self.tail.next = None
            self.lenght -= 1

    def delete_node_from_position(self, pos):
        if pos == 0:
            self.delete_node_from_head()
        elif pos + 1 == self.lenght:
            self.delete_node_from_tail()
        elif pos <= self.lenght:
            current_node = self._get_node_by_position(pos)
            current_node.previous.next = current_node.next
            current_node.next.previous = current_node.previous
            self.lenght -= 1

    def pprint(self):
        print('>>> HEAD: {}'.format(self.head))
        print('>>> TAIL: {}'.format(self.tail))
        print('>>> Lenght: {}'.format(self.lenght))

        if not self.is_empty():
            print('>>> Elements:')
            print('    Number 0 is:')
            self.print_node(self.head)
            current_node = self.head
            for num in range(1, self.lenght):
                print('    Number {} is:'.format(num))
                current_node = current_node.next
                self.print_node(current_node)

    @staticmethod
    def print_node(node):
        try:
            prev = node.previous
            next = node.next
            print('        {}  <--|{}|-->  {}'.format(prev, node.value, next))
        except Exception as e:
            print('        Exception raise on node: |{}|'.format(node))
            print('        {}'.format(e))


def main():
    blink = BLinkedList()
    blink.pprint()

    print('-' * 80)
    blink.add_node_to_head(4)
    blink.pprint()

    print('-' * 80)
    blink.add_node_to_head(17)
    blink.add_node_to_head(170)
    blink.pprint()
    # [170, 17, 4]

    print('-' * 80)
    blink.add_node_to_tail(16)
    blink.add_node_to_tail(165)
    blink.pprint()
    # [170, 17, 4, 16, 165]

    print('-' * 80)
    blink.add_node(16, 0)
    blink.pprint()
    # [16, 170, 17, 4, 16, 165]

    print('-' * 80)
    blink.add_node(155, 6)
    blink.pprint()
    # [16, 170, 17, 4, 16, 165, 155]

    print('-' * 80)
    blink.add_node(34, 3)
    blink.pprint()
    # [16, 170, 17, 34, 4, 16, 165, 155]

    print('-' * 80)
    blink.delete_node_from_head()
    blink.pprint()
    # [170, 17, 34, 4, 16, 165, 155]

    print('-' * 80)
    blink.delete_node_from_tail()
    blink.pprint()
    # [170, 17, 34, 4, 16, 165]

    print('-' * 80)
    blink.delete_node_from_position(3)
    blink.pprint()
    # [170, 17, 34, 16, 165]

    print('-' * 80)
    blink.delete_node_from_position(2)
    blink.pprint()
    # [170, 17, 16, 165]

    print('-' * 80)
    blink.add_node(value=12, pos=0)
    blink.pprint()
    # [12, 170, 17, 16, 165]

    print('-' * 80)
    blink.delete_node_from_position(pos=4)
    blink.pprint()
    # [12, 170, 17, 16]


if __name__ == '__main__':
    main()

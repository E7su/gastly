# -*- coding: utf-8 -*-
class SuperMassiveCircleQueue:
    '''
    Очередь на "массиве"

    Если реализовывать очередь на динамическом массиве,
    то в случае удаления элемента,
    придётся сдвигать все остальные элементы за О(n).
    Мы не будем удалять элемент из начала очереди, а будем сдвигать head.
    Таким образом мы сделаем удаление из начала очереди за О(1).
    '''

    def __init__(self, capacity=20):
        self.capacity = capacity
        self.massive = [None] * capacity
        self.head = -1
        self.tail = -1
        self.lenght = 0

    def __len__(self):
        return self.lenght

    def __str__(self):
        fullness = self.print_fullness()
        return ('>>> HEAD: {}\n'
                '>>> TAIL: {}\n'
                '>>> MASSIV: {}\n'
                '>>> FULLNESS: {}\n').format(self.head, self.tail,
                                             self.massive,
                                             fullness)

    def print_fullness(self):
        if self.lenght >= 0:
            fullness = '{filled}/{capacity}'.format(filled=self.lenght,
                                                    capacity=self.capacity)
        else:
            raise ValueError
        return fullness

    def is_empty(self):
        return self.lenght is 0

    def is_full(self):
        return self.lenght == self.capacity

    def put(self, value):
        if self.is_empty():
            self._put_if_first(value)
        elif self.is_full():
            raise IndexError
        elif self.capacity == self.tail + 1:
            self._put_to_old_redundant_nodes(value)
        else:
            self.tail += 1
            self.massive[self.tail] = value
            self.lenght += 1

    def _put_if_first(self, value):
        self.head = 0
        self.tail = 0
        self.massive[self.head] = value
        self.massive[self.tail] = value
        self.lenght += 1

    def _put_to_old_redundant_nodes(self, value):
        self.tail = 0
        self.massive[self.tail] = value
        self.lenght += 1

    def take(self):
        if self.is_empty():
            raise IndexError
        task = self.massive[self.head]
        self.head += 1
        self.lenght -= 1
        return task

    def get_top_value(self):
        return self.massive[self.head]

    def get_tail_value(self):
        return self.massive[self.tail]


def main():
    mqueue = SuperMassiveCircleQueue(2)
    print(mqueue)

    mqueue.put(4)
    print(mqueue)

    mqueue.put(124)
    print(mqueue)

    print('=' * 80)
    top_value = mqueue.get_top_value()
    print('>>> TOP:', top_value)
    print('-' * 80)
    tail_value = mqueue.get_tail_value()
    print('>>> TAIL:', tail_value)
    print('=' * 80)
    print()

    mqueue.take()
    print(mqueue)

    mqueue.put(12)
    print(mqueue)


if __name__ == '__main__':
    main()

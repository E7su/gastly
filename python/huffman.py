#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import heapq
from collections import Counter, namedtuple


class Node(namedtuple("Node", ["left", "right"])):
    # acc - префикс кода, который мы накопили, спускаясь от корня до данного узла или листа
    def walk(self, code, acc):
        self.left.walk(code, acc + "0")
        self.right.walk(code, acc + "1")

class Leaf(namedtuple("Leaf", ["char"])):
    def walk(self, code, acc):
        # записать в словарь code построенный код данного символа
        code[self.char] = acc or "0"


def huffman_encode(str):
    queue = []
    # Counter(str) сколько раз символ встретился в строке str
    for ch, freq in Counter(str).items():
        # тройка: чвстота, счтётчик, лист
        queue.append((freq, len(queue), Leaf(ch)))

    heapq.heapify(queue)

    count = len(queue)
    # пока в очереди есть хотя бы два элемента:
    while len(queue) > 1:
        # достаём элемент с минимальной частотой
        min_freq1, _count1, left = heapq.heappop(queue)
        # и следующий за ним элемент с минимальной частотой
        min_freq2, _count2, right = heapq.heappop(queue)
        heapq.heappush(queue, (min_freq1 + min_freq2, count, Node(left, right)))
        count += 1

    code = {}
    if queue:
        # корень построенного дерева
        [(_freq, _count, root)] = queue
        # обход дерева, начиная с корня
        root.walk(code, "")
    return code


def main():
    str = input()
    code = huffman_encode(str)
    encoded = "".join(code[ch] for ch in str)
    # количесто различных символов в строке и длина закодированнной строки
    print(len(code), len(encoded))
    for ch in sorted(code):
        print("{}: {}".format(ch, code[ch]))
    print(encoded)


if __name__ == "__main__":
    main()

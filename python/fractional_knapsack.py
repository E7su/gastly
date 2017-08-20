#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import heapq
import sys

"""Вычисление оптимальной стоимости вещей в рюкзаке

   Arguments:
   capacity - вместимость рюкзака (кг)
   values_and_weights - лист с парами (стоимость, вес)

   Return:
   acc - стоимость рюкзака
"""


def fractional_knapsack(capacity, values_and_weights):
    # value - стоимость предмета
    # weight - вес предмета
    # value / weight - удельная стоимость предмета
    order = [(-value / weight, weight) for value, weight in values_and_weights]
    heapq.heapify(order)

    # acc - стоимость рюкзака на данный момент
    acc = 0
    while order:
        value_per_weight, weight = heapq.heappop(order)
        # если предмет целиком убирается в рюкзак
        if weight < capacity:
            acc += -value_per_weight * weight
            capacity -= weight
        else:
            # если не умещается, то кладём сколько влезет
            acc += -value_per_weight * capacity
            break

    return acc


def main():
    reader = (tuple(map(int, line.split())) for line in sys.stdin)
    # quantity - количество элементов, capacity - вместимость рюкзака
    quantity, capacity = next(reader)
    # пары - стоимость и вес
    values_and_weights = list(reader)
    # проверка что количество пар равно количеству элементов
    assert len(values_and_weights) == quantity
    # вычисение максимальной стоимость рюкзака
    optimal_value = fractional_knapsack(capacity, values_and_weights)
    # точность до трёх знаков после запятой
    print("{:.3f}".format(optimal_value))


if __name__ == "__main__":
    main()

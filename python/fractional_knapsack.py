#!/usr/local/bin/python3
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
    # пока куча не пуста и в рюкзаке есть место
    while order and capacity:
        value_per_weight, weight = heapq.heappop(order)
        can_take = min(weight, capacity)
        acc -= value_per_weight * can_take
        capacity -= can_take

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


def test():
    assert fractional_knapsack(0, [(60, 20)]) == 0.0
    assert fractional_knapsack(25, [(60, 20)]) == 60.0
    assert fractional_knapsack(25, [(60, 20), (0, 100)]) == 60.0
    assert fractional_knapsack(25, [(60, 20), (50, 50)]) == 60.0 + 5.0

    assert fractional_knapsack(50, [(60, 20), (100, 50), (120, 30)]) == 180.0

    from random import randint
    from timing import timed
    for attempt in range(100):
        quantity = randint(1, 1000)
        capacity = randint(0, 2 * 10 ** 6)
        values_and_weights = []
        for i in range(quantity):
            values_and_weights.append(
                (randint(0, 2 * 10 ** 6), randint(1, 2 * 10 ** 6)))

        t = timed(fractional_knapsack, capacity, values_and_weights)
        assert t < 5


if __name__ == "__main__":
    main()
    # test()

# Uses python3
from itertools import count


def get_fibonacci_huge_efficient(n, m):
    return fibonacci_mod(n % pisano_period(m), m)


def pisano_period(m):
    if m == 1:
        return 1
    prev, cur = 0, 1
    for n in count(2):
        prev, cur = cur, (prev + cur) % m
        if (prev, cur) == (0, 1):
            return n - 1


def fibonacci_mod(n, m):
    if n <= 1:
        return n
    prev, cur = 0, 1
    for _ in range(n - 1):
        prev, cur = cur % m, (prev + cur) % m
    return cur


if __name__ == '__main__':
    n, m = map(int, input().split())
    print(get_fibonacci_huge_efficient(n, m))

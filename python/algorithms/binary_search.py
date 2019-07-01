import sys


def binary_search(a, param):
    l = 0
    r = len(a)
    while l < r:
        mid = (l + r) // 2
        if a[mid] > param:
            r = mid
        elif a[mid] < param:
            l = mid + 1
        else:
            return mid + 1
    return -1


def test():
    a = [1, 2, 3, 4, 5]
    print(binary_search(a, 4))
    assert binary_search(a, 4) == 4
    assert binary_search(a, 7) == -1
    b = [9]
    assert binary_search(b, 9) == 1
    c = []
    assert binary_search(c, 1) == -1


def main():
    reader = (map(int, line.split()) for line in sys.stdin)
    n, *a = next(reader)
    k, *params = next(reader)
    for param in params:
        print(binary_search(a, param), end=" ")


if __name__ == '__main__':
    main()

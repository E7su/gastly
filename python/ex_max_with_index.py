import sys


def set_input():
    input = sys.stdin

    n = int(input.readline())
    massiv_a = list(map(int, input.readline().split()))
    massiv_b = list(map(int, input.readline().split()))
    return massiv_a, massiv_b


def find_element(massiv, pattern):
    index = linear_search(massiv, pattern)
    if not index:
        index = -1
    return index


def get_max_with_index(massiv):
    local_max = 0
    for index, element in enumerate(massiv):
        if element > local_max:
            local_max = element
            index_for_max = index
    return local_max, index_for_max


def main():
    massiv_a, massiv_b = set_input()

    max_b, index_max_b = get_max_with_index(massiv_b)
    max_a, index_max_a = get_max_with_index(massiv_a[0:index_max_b])

    print('{} {}'.format(index_max_a, index_max_b))


if __name__ == '__main__':
    main()

import sys

def get_fibonacci_last_digit_efficient(n):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        current = current % 10
    return current


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    # n = int(input())
    print(get_fibonacci_last_digit_efficient(n))

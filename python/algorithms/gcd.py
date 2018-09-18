import sys


def Euclid_GCD(a, b):
    if b == 0:
        return a

    a = a % b
    return Euclid_GCD(b, a)


if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(Euclid_GCD(a, b))

# Uses python2
import sys


def Euclid_GCD(a, b):
    if b == 0:
        return a

    a = a % b
    return Euclid_GCD(b, a)


def efficient_LCM(a, b):
    LCM = a * b / Euclid_GCD(a, b)
    return LCM


if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(efficient_LCM(a, b))

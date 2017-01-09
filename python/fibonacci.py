def calc_fib(n):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for i in range(n - 1):
        previous, current = current, previous + current
    return current

r
# n = int(input('Input n: '))
n = int(input())
print(calc_fib(n))
r

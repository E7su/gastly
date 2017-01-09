def calc_fib(n):
    if (n <= 1):
        return n

    f.insert(0, 0)
    f.insert(1, 1)

    for i in range(2, n + 1):
        f.insert(i, f[i - 1] + f[i - 2])
    return f[i]


f = list()
# n = int(input('Input n: '))
n = int(input())
print(calc_fib(n))

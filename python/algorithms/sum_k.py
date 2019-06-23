def sum_k():
    n = int(input())
    i = 1
    res = []
    while n > 2 * i:
        n -= i
        res.append(i)
        i += 1

    res.append(n)
    print(i)
    print(*res)

sum_k()

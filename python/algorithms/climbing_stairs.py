import math


class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        result = 0
        k = 1
        if n % 2 == 0:
            result += 1   # for 22... combination
        for i in range(n - 1, n // 2, -1):
            result += self.get_c(i, k)  # for other combinations
            k += 1
        return int(result + 1)   # for 1111... combination

    def get_c(self, n, k):
        c = math.factorial(n)/(math.factorial(n-k) * math.factorial(k))
        return c

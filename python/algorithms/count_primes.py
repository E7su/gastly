class Solution:
    def countPrimes(self, n: int) -> int:
        is_primes = [True] * n
        if n < 2:
            return 0
        else:
            is_primes[0] = is_primes[1] = False
            for i in range(2, int(n**0.5) + 1):
                if is_primes[i]:
                    for j in range(i*i, n, i):
                        is_primes[j] = False
        return sum(is_primes)

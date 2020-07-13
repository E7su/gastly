class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        while (n > 0):
            n = n // 5
            count += n  # Number of "5" we can put in n and update n
        return count

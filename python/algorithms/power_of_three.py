## take advantage of highest limitation is 3**19 = 1162261467 since Integer has range <2147483648, so if 1162261467 % n == 0, then True
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and 1162261467 % n == 0

# class Solution:
#     def titleToNumber(self, s: str) -> int:
#         ans = 0
#         for c in s:
#             ans = ans * 26 + ord(c) - ord('A') + 1
#         return ans
class Solution:
    def titleToNumber(self, s: str) -> int:
        base = ord("A") - 1
        ret = 0
        for ch in s:
            ret *= 26
            ret += (ord(ch) - base)
            
        return ret

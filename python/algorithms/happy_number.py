# class Solution:
#     def isHappy(self, n: int) -> bool:
#         seen = set()
        
#         while True:
#             if n in seen:
#                 return False
#             elif n == 1:
#                 return True
#             else:
#                 seen.add(n)
# 				# h(x): convert int to str -> sum(foreach character in str -> int(character) ^ 2) 
#                 n = sum([int(x) ** 2 for x in str(n)])

class Solution:
    def isHappy(self, n: int) -> bool:
        while n != 1:
            n = sum([int(i) ** 2 for i in str(n)])
            if n == 4:
                return False
        
        return True


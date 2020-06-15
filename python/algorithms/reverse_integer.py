# class Solution:
#     def reverse(self, x):
#         result = 0

#         if x < 0:
#             symbol = -1
#             x = -x
#         else:
#             symbol = 1

#         while x:
#             result = result * 10 + x % 10
#             x //= 10

#         return 0 if result > pow(2, 31) else result * symbol


class Solution:
    def reverse(self, x):
        negFlag = 1
        if x < 0:
            negFlag = -1
            strx = str(x)[1:]
        else:
            strx = str(x)

        x = int(strx[::-1])
        
        return 0 if x > pow(2, 31) else x * negFlag

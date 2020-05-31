#class Solution:
#    def reverseBits(self, n: int) -> int:
#        b = bin(n)[:1:-1]
#        return int(b + '0'*(32-len(b)), 2)

class Solution:
    def reverseBits(self,n):
        res=0
        for i in range(32):
            res <<= 1
            if n & 1:  # if last bit of n is set
                res=res | 1
            n >>= 1. # right shift n
        return res

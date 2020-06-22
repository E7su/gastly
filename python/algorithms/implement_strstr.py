class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return an integer
    def strStr(self, haystack, needle):
        if haystack == needle == '':
            return 0

        size_needle = len(needle)
        size_haystack = len(haystack)
        
        for i in range(size_haystack - size_needle + 1):
            if haystack[i:i+size_needle] == needle:
                return i

        return -1

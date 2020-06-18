class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]; rtype: str
        """
        symbols_strings = zip(*strs)
        ret = ""
        # looping corrected based on @StefanPochmann's comment below
        for symbols in symbols_strings:
            if len(set(symbols)) > 1:
                break
            ret += symbols[0]
        return ret

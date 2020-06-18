class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]; rtype: str
        """
        # [('f', 'f', 'f'), ('l', 'l', 'l'), ('o', 'o', 'i'), ('w', 'w', 'g')]
        symbols_strings = zip(*strs)
        print(list(symbols_strings))
        ret = ""
        for symbols in symbols_strings:
            if len(set(symbols)) > 1:  # ('o', 'o', 'i')
                break
            ret += symbols[0]
        return ret

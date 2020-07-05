class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s = s.lower()
        # s = [char for char in s if char.isalnum()]
        # return s == s[::-1]

        flag = True
        newStr = re.sub('[^A-Za-z0-9]+', '', s)
        start, end = 0, len(newStr) - 1
        while start < end:
            if newStr[start].lower() != newStr[end].lower():
                flag = False
                break;
            else:
                start += 1
                end -= 1
        return flag

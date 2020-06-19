class Solution:
    def isValid(self, s: str) -> bool:
        valid_parentheses = {'{': '}', '(': ')', '[': ']'}
        stack = []

        for i in s:
            if i in valid_parentheses:
                stack.append(i)
            elif len(stack):
                if valid_parentheses[stack.pop()] != i:
                    return False
            else:
                return False
        if len(stack) == 0:
            return True

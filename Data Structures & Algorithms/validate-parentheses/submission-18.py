class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parens = {')':'(',']':'[','}':'{'}

        for l in s:
            if l in parens:
                if stack and stack[-1] == parens[l]:
                    stack.pop()
                else:
                    return False
            else: 
                stack.append(l)
        return not stack
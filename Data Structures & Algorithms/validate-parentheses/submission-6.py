class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        stack = ''
        j = (len(s))
        for i in range(j):
            if (s[i] == ')' or s[i] == ']' or s[i] == '}') and stack == '':
                return False
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack = stack + s[i]
            if (s[i] == ')' or s[i] == ']' or s[i] == '}') and stack != '':
                if s[i] == ')':
                    if stack[-1] == '(':
                        stack = stack [:-1]
                    else:
                        return False
                if s[i] == ']':
                    if stack[-1] == '[':
                        stack = stack [:-1]
                    else:
                        return False
                if s[i] == '}':
                    if stack[-1] == '{':
                        stack = stack [:-1]
                    else:
                        return False
        if stack == '':
            return True
        else:
            return False  
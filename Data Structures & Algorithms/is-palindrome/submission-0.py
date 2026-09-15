class Solution:
    def isPalindrome(self, s: str) -> bool:
        b = ''
        for i in range(len(s)):
            if s[i].isalnum():
                b = b + s[i].lower()
        print(b)
        if b == b[::-1]:
            return True
        else: 
            return False
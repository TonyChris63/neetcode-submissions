class Solution:
    def isPalindrome(self, s: str) -> bool:
        b = ''
        for l in s:
            if l.isalnum():
                b += l.lower()
        return b == b[::-1]
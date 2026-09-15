class Solution:
    def isPalindrome(self, s: str) -> bool:
        b = ''
        for i in range(len(s)):
            if s[i].isalnum():
                b += s[i].lower()
        return b == b[::-1]
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        s1 = {}
        t1 = {}
        for char in s:
            s1[char] = s1.get(char, 0) + 1
        for char in t:
            t1[char] = t1.get(char, 0) + 1
        return s1 == t1
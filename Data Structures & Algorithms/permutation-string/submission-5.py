class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c1 = [0] * 26
        c2 = [0] * 26
        l = 0

        for z in s1:
            c1[ord(z) - ord('a')] += 1

        for r in range(len(s2)):
            c2[ord(s2[r]) - ord('a')] += 1
            if r - l + 1 > len(s1):
                c2[ord(s2[l]) - ord('a')] -= 1
                l += 1
            if c1 == c2:
                return True
        
        return False
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        maxl = 0
        i = 0
        
        for j in range(len(s)):
            while s[j] in seen:
                seen.remove(s[i])
                i += 1
            seen.add(s[j])
            maxl = max(maxl, j - i + 1)
        return maxl
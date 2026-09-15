class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        i = 0
        maxl = 0

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[i])
                i += 1
            seen.add(s[r])
            maxl = max(maxl, r - i + 1)

        return maxl


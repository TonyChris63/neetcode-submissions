class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        maxl = 0
        count = {}

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            if (r - l) - max(count.values()) < k:
                maxl = max(maxl, r - l + 1)
            else:
                count[s[l]] -= 1
                l += 1

        return maxl
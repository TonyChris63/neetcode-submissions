class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        store = set(nums)
        res = 0

        for n in nums:
            length = 1
            if n - 1 not in store:
                while n + length in store:
                    length += 1
                res = max(res,length)

        return res
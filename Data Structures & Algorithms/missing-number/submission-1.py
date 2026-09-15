class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        m = len(nums)
        s = sum(nums)
        s0 = 0
        m1 = m
        for i in range(m):
            s0 += m1
            m1 = m1 - 1
        return s0 - s

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        a = 1
        b = 1
        if len(nums) == 0:
            return 0
        for i in range(len(nums)-1):
            if nums[i+1] == nums[i]:
                continue
            elif (nums[i+1] - nums[i]) == 1:
                a = a + 1
            else:
                b = max(a, b)
                a = 1
        return max(a, b)
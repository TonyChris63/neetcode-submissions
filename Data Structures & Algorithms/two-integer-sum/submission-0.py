class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compv = {}
        for i in range(len(nums)):
            num = nums[i]
            if target - num in compv:
                return [compv[target - num], i]
            compv[num] = i
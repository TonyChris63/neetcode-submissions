class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compv = {}

        for i,n in enumerate(nums):
            diff = target - n
            if diff in compv:
                return [compv[diff], i]
            else:
                compv[n] = i
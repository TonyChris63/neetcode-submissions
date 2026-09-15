class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n2 = set(nums)
        if len(n2) == len(nums):
            return False
        else:
            return True
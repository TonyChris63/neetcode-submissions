class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        m = len(nums)
        s = sum(nums)
        s1 = ((m)*(m+1))/2
        return int(s1 - s)

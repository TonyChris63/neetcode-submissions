class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        zcount = 0
        zind = 0
        prod = 1
        for i in range(len(nums)):
            if nums[i] == 0:
                zcount += 1
                zind += i
        if zcount > 1:
            ans = [0] * len(nums)
        elif zcount == 1:
            nums[zind] = 1
            for n in nums:
                prod *= n
            ans = [0] * len(nums)  
            ans[zind] = prod
        else:
            for n in nums:
                prod *= n
            for n in nums:
                ans.append(prod//n)
        return ans
            
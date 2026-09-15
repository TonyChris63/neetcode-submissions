class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        prod = 1
        prod0 = 1
        zcount = 0
        for n in nums:
            prod *= n
            if n != 0:
                prod0 *= n
            else:
                zcount += 1
        if prod == 0:
            if zcount > 1:
                ans = [0] * len(nums)
            else:
                for i in range(len(nums)):
                    if nums[i] == 0:
                        ans.append(prod0)
                    else:
                        ans.append(prod)
        else:
            for i in range(len(nums)):
                ans.append(int(prod/nums[i]))
        return ans
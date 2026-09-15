class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        ind = 0
        res = float('inf')

        while l <= r:
            if nums[l] < nums[r]:
                if nums[l] < res:
                    res = nums[l]
                    ind = l
                break
            m = l + (r - l) // 2
            if nums[m] < res:
                res = nums[m]
                ind = m
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        
        l = 0
        r = len(nums) - 1

        while l <= r:
            v = l + (r - l) // 2
            h = (v + ind) % len(nums)
            if nums[h] == target:
                return h
            elif nums[h] > target:
                r = v - 1
            else:
                l = v + 1

        return -1
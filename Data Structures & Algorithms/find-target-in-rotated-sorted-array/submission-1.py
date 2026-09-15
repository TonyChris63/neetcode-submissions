class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        ind = 0
        res = float('inf')

        while l <= r:
            if nums[l] < nums[r]:
                if nums[l] < res:
                    ind = l
                    res = nums[l]
                break
            
            m = l + (r - l) // 2
            if nums[m] < res:
                ind = m
                res = nums[m]
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        
        s = 0
        e = len(nums) - 1

        while s <= e:
            h = s + (e - s) // 2
            v = (h + ind) % len(nums)

            if nums[v] == target:
                return v
            elif nums[v] > target:
                e = h - 1
            else:
                s = h + 1

        return -1
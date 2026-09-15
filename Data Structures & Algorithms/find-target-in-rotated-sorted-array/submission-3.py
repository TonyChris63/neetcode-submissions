class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        min1 = float('inf')
        ind = 0

        while l <= r:
            if nums[l] < nums[r]:
                if nums[l] < min1:
                    ind = l
                    min1 = nums[l]
            
            m = l + (r - l) // 2
            if nums[m] < min1:
                ind = m
                min1 = nums[m]
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        
        l = 0
        r = len(nums) - 1

        while l <= r:
            h = l + (r - l) // 2
            v = (h + ind) % len(nums)

            if nums[v] == target:
                return v
            elif nums[v] > target:
                r = h - 1
            else:
                l = h + 1
        
        return -1
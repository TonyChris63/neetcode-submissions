class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        l = 0
        r = len(height) - 1
        leftmax = height[l]
        rightmax = height[r]

        while l < r:
            if leftmax < rightmax:
                l += 1
                leftmax = max(leftmax,height[l])
                total += leftmax - height[l]
            else:
                r -= 1
                rightmax = max(rightmax, height[r])
                total += rightmax - height[r]
        
        return total
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxA = 0

        l = 0
        r = len(heights) - 1

        while l < r:
            width = r - l
            height = min(heights[l],heights[r])
            area = width * height
            maxA = max(maxA, area)

            if heights[l] == height:
                l += 1
            elif heights[r] == height:
                r -= 1
            
        return maxA
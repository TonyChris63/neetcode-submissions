class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start = 0
        end = len(heights) - 1
        maxA = 0
        
        while start < end:
            width = end - start
            length = min(heights[start], heights[end])
            maxA = max(maxA, width * length)
            
            if heights[start] < heights[end]:
                start += 1
            else:
                end -= 1

        return maxA

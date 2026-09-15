class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        l = 0
        r = (rows * cols) - 1

        while l <= r:
            mid = l + ((r - l)//2)
            ro = mid // cols
            co = mid % cols

            print((ro,co))

            if matrix[ro][co] == target:
                return True
            elif matrix[ro][co] > target:
                r = mid - 1
            else:
                l = mid + 1

        return False
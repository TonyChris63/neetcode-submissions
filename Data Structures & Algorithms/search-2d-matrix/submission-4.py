class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        startr = 0
        endr = rows - 1
        start = 0
        end = cols - 1

        while startr <= endr:
            midr = (startr + endr) // 2
            if matrix[midr][-1] < target:
                startr = midr + 1
            elif matrix[midr][0] > target:
                endr = midr - 1
            else:
                break

        if not (startr <= endr):
            return False
        row = (startr + endr)//2
        while start <= end:
            mid = (start + end) // 2
            if matrix[row][mid] < target:
                start = mid + 1
            elif matrix[row][mid] > target:
                end = mid - 1
            else:
                return True
        return False
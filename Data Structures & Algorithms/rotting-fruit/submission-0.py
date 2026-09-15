class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        visit = set()
        dist = 10
        maxD = 0

        def addCell(r,c):
            if min(r,c) < 0 or r == rows or c == cols or (r,c) in visit or grid[r][c] == 0:
                return
            visit.add((r,c))
            q.append((r,c))
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i,j))
                    visit.add((i,j))

        while q:
            for u in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = dist
                addCell(r+1,c)
                addCell(r,c+1)
                addCell(r-1,c)
                addCell(r,c-1)
            dist += 1
        
        for p in range(rows):
            for g in range(cols):
                if grid[p][g] > 0:
                    if grid[p][g] == 1:
                        return -1
                    else:
                        maxD = max(maxD, (grid[p][g] - 10))

        return maxD
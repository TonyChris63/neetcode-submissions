class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        visit = set()
        dist = 0

        def addCell(r,c):
            if min(r,c) < 0 or r == rows or c == cols or (r,c) in visit or grid[r][c] == -1:
                return
            q.append((r,c))
            visit.add((r,c))


        for l in range(rows):
            for m in range(cols):
                if grid[l][m] == 0:
                    visit.add((l,m))
                    q.append((l,m))
        
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = dist
                addCell(r+1,c)
                addCell(r,c+1)
                addCell(r-1,c)
                addCell(r,c-1)
            dist += 1




    
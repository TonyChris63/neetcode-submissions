class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        current = 0
        maxI = 0

        def bfs(i,j):
            q = deque()
            q.append((i,j))
            curr = 1
            grid[i][j] = 0
            directions = [(0,1),(1,0),(0,-1),(-1,0)]
            while q:
                x,y = q.popleft()
                for r,c in directions:
                    nx = x + r
                    ny = y + c
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                        q.append((nx,ny))
                        curr += 1
                        grid[nx][ny] = 0
            return curr

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    current = bfs(i,j)
                    maxI = max(maxI,current)
                    current = 0
        return maxI
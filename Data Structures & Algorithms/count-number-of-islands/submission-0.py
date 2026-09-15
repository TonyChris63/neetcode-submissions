class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        island = 0

        def bfs(i,j):
            q = deque()
            q.append((i,j))
            grid[i][j] = '0'
            directions = [(0,1),(1,0),(0,-1),(-1,0)]

            while q:
                x,y = q.popleft()
                for r,c in directions:
                    nx = x + r
                    ny = y + c
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == '1':
                        q.append((nx,ny))
                        grid[nx][ny] = '0'

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    bfs(i,j)
                    island += 1

        return island
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        island = 0
        #Breadth First Search
        def bfs(i,j):
            #Make a dual sided queue, doubly linked list
            q = deque()
            #Add i,j coordinates 
            q.append((i,j))
            #since it is visited mark it 0 as visitedd
            grid[i][j] = '0'
            #these are the four directions in which you will travel
            directions = [(0,1),(1,0),(0,-1),(-1,0)]

            #while there is something in the deque
            while q:
                #make x and y become i and j, and remove what you just visited
                x,y = q.popleft()
                #going through all directional possibilities by creating new variables for each
                for r,c in directions:
                    #do it for x
                    nx = x + r
                    #do it for y
                    ny = y + c
                    #if the new x and new y are within where they can be and its still land
                    #add that new place into the deque and mark it 0 as seen
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == '1':
                        q.append((nx,ny))
                        grid[nx][ny] = '0'
        #look for land and perform the algorithm                
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    bfs(i,j)
                    island += 1

        return island
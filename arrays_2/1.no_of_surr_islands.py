class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        def dfs(grid,x,y,visited):
            ans = False
            visited.add((x,y))
            directions = [[-1,0],[1,0],[0,1],[0,-1]]
            for way in directions:
                i,j = way[0],way[1]
                xn = x+i
                yn = y+j
                if (xn,yn) not in visited and  0<=xn<len(grid) and 0<=yn<len(grid[0]) and grid[xn][yn]==0:
                    ans = dfs(grid,xn,yn,visited) or ans
                
                elif xn<0 or xn>=len(grid) or yn<0 or yn>len(grid[0])-1:
                    ans = True
            return ans

        visited = set()
        c = 0
        n = len(grid)
        m = len(grid[0])
        for x in range(1,n-1):
            for y in range(1,m-1):
                if grid[x][y]==0 and (x,y) not in visited:
                    if dfs(grid,x,y,visited):
                        continue
                    else:
                        c+=1
        
        return c
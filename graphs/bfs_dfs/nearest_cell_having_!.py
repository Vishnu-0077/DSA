def dfs(matrix,x,y,visited,count):
    if matrix[x][y] == 1:
        return count
    directions = [[-1,0],[1,0],[0,-1],[0,1]]
    mini = float('inf')
    for way in directions:
        i,j = way[0],way[1]
        if 0<=x+i<len(matrix) and 0<=y+j<len(matrix[0]) and (x+i,y+j) not in visited:
            visited.add((x+i,y+j))
            result = dfs(matrix,x+i,y+j,visited,count+1)
            mini = min(mini,result)
            visited.remove((x+i,y+j))
    return mini

def main(matrix):
    ans = []
    for i in range(len(matrix)):
        ans.append([])
        for j in range(len(matrix[0])):
            ans[i].append(0)

    for xr in range(len(matrix)):
        for yr in range(len(matrix[0])):
            if matrix[xr][yr] == 1:
                ans[xr][yr] = 0
                continue
            else:
                visited = set()
                visited.add((xr,yr))
                count = 0
                value = dfs(matrix,xr,yr,visited,count)
                ans[xr][yr] = value
    return ans

if __name__ == '__main__':
    matrix = [
        [0, 1, 1, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 1]
    ]

    for x in matrix:
        print(x)

    print()
        
    ans = main(matrix)
    for x in ans:
        print(x)
            
    
def dfs(matrix,x,y,visited,count): #here in this dfs we are counting everymin as we progress so we are counting inside the dfs
    visited.add((x,y))
    maxi=count
    for i in range(-1,2):
        for j in range(-1,2):
            if abs(j-i) == 1 and (0<=x+i<len(matrix[0])) and (0<=y+j<len(matrix))and matrix[x+i][y+j] ==1 and (x+i,y+j) not in visited:
                matrix[x+i][y+j] = 2
                result = dfs(matrix,x+i,y+j,visited,count+1)
                maxi = max(maxi,result)
    return maxi


def main(matrix): #in no of connected we counted no of paths, so we counted outside the dfs
    visited = set()
    max_count = 0
    for x in range(len(matrix[0])):
        for y in range(len(matrix)):
            if matrix[x][y] == 2:
                max_count = max(max_count,dfs(matrix,x,y,visited,0)) #maxi and max_count are different....
    for x in matrix: #maxi is max count of branched paths.... max_count is max of entirely new path
        for y in x:
            if y == 1:
                return -1
    return max_count

grid = [ [2,1,1] , [1,1,0] , [0,1,1] ]
for x in grid:
    print(x)
print(main(grid))

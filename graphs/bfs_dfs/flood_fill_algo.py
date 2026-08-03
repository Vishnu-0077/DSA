def dfs(matrix,x,y,new,exist,visited):
    visited.add((x,y))
    directions = [[1,0],[-1,0],[0,1],[0,-1]] #new way to move in different directions
    for way in directions:
        i,j = way[0],way[1]
        if 0<=x+i<len(matrix[0]) and 0<=y+j<len(matrix) and matrix[x+i][y+j] == exist and (x+i,y+j) not in visited:
            matrix[x+i][y+j] = new
            dfs(matrix,x+i,y+j,new,exist,visited)

def main(matrix,sr,sc,newcolor):
    exist = matrix[sr][sc]
    new = newcolor
    matrix[sr][sc] = new
    visited = set()
    dfs(matrix,sr,sc,new,exist,visited)
    return matrix

matrix = [[1,1,1],
          [2,2,0],
          [2,2,2]]
sr = 2
sc = 0
newcolor = 3
for x in matrix:
    print(x)
new_matrix = main(matrix,sr,sc,newcolor)
print()
for x in new_matrix:
    print(x)

    
def sol(matrix):
    store = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]==0:
                store.append((i,j))
    for p in store:
        x,y = p
        for i in range (len(matrix)):
            matrix[i][y]=0
        for j in range (len(matrix[0])):
            matrix[x][j]=0
    return matrix

matrix=[[1,1,1],[1,0,1],[1,1,1]]
print(sol(matrix))
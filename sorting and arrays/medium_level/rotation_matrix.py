def rotate(matrix):
    ans = [[0]*len(matrix[0]) for i in range(len(matrix))]
    for j in range(len(matrix[0])):
        for i in range(len(matrix)-1,-1,-1):
            ans[j][len(matrix)-i-1] = matrix[i][j]
    return ans

matrix = [[0, 1, 1, 2], [2, 0, 3, 1], [4, 5, 0, 5], [5, 6, 7, 0]]
print(rotate(matrix))



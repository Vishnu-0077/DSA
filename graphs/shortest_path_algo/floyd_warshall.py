def floyd_method(matrix):
    n=len(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j]==-1:
                matrix[i][j] = float('inf')

    for via in range(len(matrix)):
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                result = matrix[i][via]+matrix[via][j]
                matrix[i][j] = min(result,matrix[i][j])
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == float('inf'):
                matrix[i][j] = -1
    return matrix

if __name__ == '__main__':
    matrix = [[0, 2, -1, -1], [1, 0, 3, -1], [-1, -1, 0, 1], [3, 5, 4, 0]]
    print(floyd_method(matrix))
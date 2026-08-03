def dfs(matrix,node,visited):
    visited.add(node)
    for neighbour in range(len(matrix[node])):
        if matrix[node][neighbour] == 1 and neighbour not in visited:
            dfs(matrix,neighbour,visited)

def remove_diagonal(matrix):
    for i in range(len(matrix)):
        matrix[i][i] = 0
    return matrix

def main(matrix):
    visited = set()
    count = 0
    for node in range(len(matrix)):
        if node not in visited:
            dfs(matrix,node,visited)
            count +=1
    return count

adj=[ [1, 0, 1], [0, 1, 0], [1, 0, 1] ]
matrix = remove_diagonal(adj)

for x in matrix:
    print(x)
print(main(matrix))

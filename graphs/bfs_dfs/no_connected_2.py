def create_matrix(v):
    matrix = []
    for i in range(v):
        matrix.append([])
    for i in range(v):
        for j in range(v):
            matrix[i].append(0)
    return matrix
def add_edge(matrix,u,v):
    matrix[u][v] = 1
    matrix[v][u] = 1

def dfs(matrix,node,visited): #do not have to return dfs is not needed
    visited.add(node)
    for neighbour in range(len(matrix[node])):
        if matrix[node][neighbour] == 1 and neighbour not in visited:
            dfs(matrix,neighbour,visited)

def main(matrix):
    visited = set()
    count = 0

    for node in range(len(matrix)):
        if node not in visited:
            dfs(matrix,node,visited)
            count +=1
    return count

v=4
edges=[[0,1],[1,2]]
matrix = create_matrix(v)
for x in edges:
    add_edge(matrix,x[0],x[1])
for x in matrix:
    print(x)
print(main(matrix))

#--------------------------------------BFS meethod

def dic(edges,v):
    dic = {}
    for i in range(v):
        dic[i] = []
    for x in edges:
        dic[x[0]].append(x[1])
        dic[x[1]].append(x[0])
    return dic

def bfs(dic,v):
    visited = set()
    count=0
    for i in range(v):
        if i in visited:
            continue
        start = i
        stack = [start]
        count+=1
        while stack:
            node = stack.pop()
            for neighbour in dic[node]:
                if neighbour not in visited:
                    stack.append(neighbour)
                    visited.add(neighbour)
    return count

print(bfs(dic(edges,v),v))




    
    
def dfs(graph,node,visited,ans):
    if node in visited:
        return
    ans.append(node)
    visited.add(node)
    for neighbour in graph[node]:
        dfs(graph,neighbour,visited,ans)

def dfs_matrix(matrix, node, visited): #this code works for the dfs matrixxx
    visited.add(node)

    for neighbour in range(len(matrix)):
        if matrix[node][neighbour] == 1 and neighbour not in visited:
            dfs_matrix(matrix, neighbour, visited)

    
visited = set()
ans = []

graph = {1:[2,6], 2:[1,3,4] , 6:[1,7,9], 4:[2,5], 5:[4,8] , 7:[6,8] , 9:[6], 8:[5,7], 3:[2] }

dfs(graph,1,visited,ans)
print(ans)
    
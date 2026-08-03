#same as the topological sorting

def dfs(matrix,node,visited,stack):
    visited.add(node)
    for neighbour in matrix[node]:
        if neighbour not in visited:
            dfs(matrix,neighbour,visited,stack)
    stack.append(node)

def main(matrix,n):
    visited = set()
    stack = []
    for node in range(n):
        if node not in visited:
            dfs(matrix,node,visited,stack)
    return stack

if __name__ == '__main__':
    matrix = [[1,0],[2,1],[3,2]]
    n = 4
    adj = []
    for i in range(n):
        adj.append([])
    for u,v in matrix:
        adj[u].append(v)
    print(main(adj,n))
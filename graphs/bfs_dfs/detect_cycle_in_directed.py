def dfs(matrix,node,visited):
    visited.add(node)
    for neighbour in matrix[node]:
        if neighbour not in visited:
            return dfs(matrix,neighbour,visited)
        else:
            return False
    return True

def main(matrix,n):
    for node in range(n):
        visited = set()
        if dfs(matrix,node,visited):
            continue
        else:
            return True
    return False
            


if __name__ == '__main__':
    
    n = 5
    adj = [[] for _ in range(n)]
    adj[0].append(1)
    adj[1].append(2)
    adj[2].append(3)
    adj[3].append(4)
    adj[4].append(1) 
    print(adj)
    print()
        
    if main(adj,n):
        print('cycle')
    else:
        print('no cycle')
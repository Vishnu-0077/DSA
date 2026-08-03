def dfs(matrix,node,visited,count):
    if node == 2:
        return count
    visited.add(node)
    mini = float('inf')
    for x,y in matrix[node]:
        if x not in visited:
            dist = y
            result = dfs(matrix,x,visited,count+dist)
            mini = min(mini,result)
    visited.remove(node) #in cyclic graph have to remove node
    return mini

def main(matrix,n):
    ans = []
    for node in range(n):
        visited = set()
        counted = dfs(matrix,node,visited,0)
        ans.append(counted)
    return ans

if __name__ == "__main__":
    n = 3
    adj = [[] for _ in range(n)]
    adj[0].append((1,1))
    adj[0].append((2,6))
    adj[1].append((2,3))
    adj[1].append((0,1))
    adj[2].append((1,3))
    adj[2].append((0,6))
    print(adj)
    print(main(adj,n))
    
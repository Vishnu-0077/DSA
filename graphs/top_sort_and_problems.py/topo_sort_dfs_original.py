def dfs(matrix,node,visited,stack):
    visited.add(node)
    for neighbour in matrix[node]:
        if neighbour not in visited:
            dfs(matrix,neighbour,visited,stack)
    stack.append(node)
    
def main(matrix):
    visited = set()
    stack = []
    n=len(matrix)
    for node in range(n):
        if node not in visited:
            dfs(matrix,node,visited,stack)
    return stack[::-1]

if __name__ == '__main__':
    adj = [[2], [], [1], [],[]] 
    print(main(adj))

#-----bfs------

def bfs(adj):
    ans = []
    visited = set()
    for i in range(len(adj)):
        stack = []
        small_ans = []
        if i not in visited:
            stack.append(i)
        while stack:
            node = stack.pop(0)
            small_ans.append(node)
            for neighbour in adj[node]:
                if neighbour not in visited:
                    stack.append(neighbour)
            visited.add(node)
        for p in small_ans[::-1]:
            ans.append(p)
    return ans[::-1]

print(bfs(adj))
        
            

        
def dfs(matrix,node,visited,colour_visited,node_colour):
    actual_colour = (-1)**node_colour
    visited.add(node)
    colour_visited.add((node,actual_colour))
    for neighbour in matrix[node]:
        if neighbour not in visited:
            return dfs(matrix,neighbour,visited,colour_visited,node_colour+1)
        elif (neighbour,actual_colour) in colour_visited: #actually it should be not in(by understanding).... but as we update the actual_color above
            return False                                  # we are putting neighbour in.....
    return True

def main(matrix,n):
    visited = set()
    colour_visited = set()
    for node in range(n):
        if node not in visited:
            if dfs(matrix,node,visited,colour_visited,0):
                continue
            else:
                return False
    return True

if __name__ == "__main__":
    n = 10
    adj = [[] for _ in range(n)]
    
    adj[0].append(1)
    adj[1].append(2)
    adj[2].append(3)
    adj[3].append(4)
    adj[4].append(5)
    adj[5].append(6)
    adj[5].append(8)
    adj[6].append(7)
    adj[7].append(2)
    adj[8].append(9)

    print(adj)
    print()
        
    if main(adj,n):
        print('bipartite')
    else:
        print('not bipartite')
        
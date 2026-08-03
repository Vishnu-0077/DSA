def bfs(adj,start,visited):
    queue = []
    queue.append(start)
    before = -1
    while queue:
        node = queue.pop(0)
        for neighbour in adj[node]:
            if neighbour != before:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)
                else:
                    return False
        before = node
    return True

def main(adj,V):
    visited = set()
    for start in range(V):
        if start not in visited:
            visited.add(start)
            if not bfs(adj,start,visited):
                return False
    return True




V = 5
adj = [[] for _ in range(V)]

    # Add edges
adj[0].append(1)
adj[1].append(0)
adj[1].append(2)
adj[2].append(1)
adj[2].append(3)
adj[3].append(2)
adj[3].append(4)
adj[4].append(3)

print(adj)
print()
if not main(adj,V):
    print('there is a cycle')
else:
    print('no cycle')
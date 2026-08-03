graph = {}

graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []

def bfs(graph,start): #level by level
    #do this using the queue method
    queue = []
    visited = set()
    queue.append(start)
    while queue:
        node = queue.pop(0)
        print(node,end=" ")
        for neighbour in graph[node]:
            if neighbour not in visited:
                queue.append(neighbour)
                visited.add(neighbour)

def bfs_not_level(graph, start): #not level by level #failure
    stack = []
    visited = set()
    stack.append(start)
    while stack:
        node = stack.pop()
        print(node,end = ' ')
        for x in graph[node]:
            if x not in visited:
                stack.append(x)
                stack.append(x)
                break

def dfs(graph,node,visited = set()):
    if node in visited:
        print(end='-')
        return
    visited.add(node)
    print(node,end=" ")
    for neighbour in graph[node]:
        dfs(graph,neighbour)




bfs(graph,'you')
print()
dfs(graph,'you')
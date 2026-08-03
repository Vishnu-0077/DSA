#in bfs always use a queue system. right???

def bfs(graph,start):
    queue = []
    ans = []
    visited = set()
    queue.append(start)
    visited.add(start)
    while queue:
        node = queue.pop(0)
        ans.append(node)
        for x in graph[node]:
            if x not in visited:
                visited.add(x)
                queue.append(x)
    
    return ans

graph = {1:[2,6], 2:[1,3,4] , 6:[1,7,9], 4:[2,5], 5:[4,8] , 7:[6,8] , 9:[6], 8:[5,7], 3:[2] }
print(bfs(graph, 1))

    
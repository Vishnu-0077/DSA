def is_safe(graph,colour,col):
    for neigh in graph[col]:
        if colour[neigh] == col:
            return False
    return True

def rec(graph,colour,node,n,m):
    if node==n:
        return True
    for col in range(m):
        if is_safe(graph,colour,col):
            colour[node] = col

            if rec(graph,colour,node+1,n,m):
                return True
            colour[node] = -1
    return False

n = 4
m = 2
colour = [0] * n
graph = [
    [1, 2],
    [0, 2],
    [0, 1]
]
print(rec(graph,colour,0,n,m))


def graph(n):
    graph = []
    for i in range(n):
        graph.append([])
        for j in range(n):
            graph[i].append(0)
    return graph

def add_edge(graph,u,v):
    graph[u][v] = 1
    graph[v][u] = 1
    return graph

def remove_edge(graph,u,v):
    graph[u][v] = 0
    graph[v][u] = 0
    return graph

def add_node(graph):
    graph.append([])
    for i in range(len(graph)-1):
        graph[-1].append(0)
    for i in range(len(graph)):
        graph[i].append(0)
    return graph


g = graph(5)

for x in g:
    print(x)
g = add_node(g)

for x in g:
    print(x)
import heapq

def prims(adj):
    heap = []
    visited = set()
    summ = 0
    mst = []
    heapq.heappush(heap,[0,0,-1])
    while heap:
        dist,node,prev = heapq.heappop(heap)
        if node in visited:
            continue
        visited.add(node)
        if prev != -1:
            mst.append([prev,node,dist])
            summ += dist
        for neigh in adj[node]:
            heapq.heappush(heap,[neigh[1],neigh[0],node])
    return summ,mst

def format(adj):
    dic = {}
    for node in adj:
        if node[0] not in dic:
            dic[node[0]] = []
        dic[node[0]].append([node[1],node[2]])
        if node[1] not in dic:
            dic[node[1]] = []
        dic[node[1]].append([node[0],node[2]])
    return dic
adj = edges = [
    [0, 1, 2],
    [0, 3, 6],
    [1, 2, 3],
    [1, 3, 8],
    [1, 4, 5],
    [4, 2, 7]
]
adj = format(adj)
print(prims(adj))

def disjoint_set(n):
    parent = []
    for i in range(n):
        parent.append(i)
    rank = [0]*(n)
    return parent,rank

def find_parent(parent,i):
    if parent[i] == i:
        return i
    parent[i] = find_parent(parent,parent[i])
    return parent[i]

def union_by_rank(u,v,parent,rank):
    pu = find_parent(parent,u)
    pv = find_parent(parent,v)

    if pu==pv:
        return
    if rank[pu]<rank[pv]:
        parent[pu]=pv
    elif rank[pv]<rank[pu]:
        parent[pv]=pu
    else:
        parent[pu]=pv
        rank[pv]+=1

def connect(n,m,edges):
    parent,rank = disjoint_set(n)
    for u,v in edges:
        union_by_rank(u,v,parent,rank)
    nc = 0
    for i in range(n):
        if find_parent(parent,i)==i:
            nc+=1
    if m<nc:
        return -1
    return nc-1

Edge =[ [0,  1], [ 0, 2], [1, 2]]
print(connect(4,3,Edge))

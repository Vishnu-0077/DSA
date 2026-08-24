def disjoint_set(n):
    parent = []
    for i in range(n):
        parent.append(i)
    rank = [0]*(n)
    return parent,rank

def find_par(parent,i):
    if parent[i] == i:
        return i
    parent[i] = find_par(parent,parent[i])
    return parent[i]

def union_rank(parent,rank,u,v):
    pu = find_par(parent,u)
    pv = find_par(parent,v)
    if pu==pv:
        return

    if rank[pu]>rank[pv]:
        parent[pv] = pu
    elif rank[pu]<rank[pv]:
        parent[pu] = pv
    else:
        parent[pv] = pu
        rank[pu] += 1

def kruskals(adj,n):
    parent,rank = disjoint_set(n)
    ans = 0
    mst = []
    for u,v,w in adj:
        if find_par(parent,u)!=find_par(parent,v):
            union_rank(parent,rank,u,v)
            ans += w
            mst.append([u,v,w])
        if len(mst)==len(adj)-1:
            break

    return ans,mst

edges = [[0,1,2],[0,3,6],[1,2,3],[1,3,8],[1,4,5],[4,2,7]]
n=9
print(kruskals(edges,n))

def disjoint_set(n):
    parent = []
    for i in range(n+1):
        parent.append(i)
    rank = [0]*(n+1)
    return parent,rank

def find_par(parent,i):
    if parent[i] == i:
        return i
    return find_par(parent,parent[i])

def find_par_with_path_compress(parent,i):
    if parent[i]==i:
        return i
    parent[i] = find_par_with_path_compress(parent,parent[i])
    return parent[i]

def union_by_rank(u,v,parent,rank):
    pu = find_par_with_path_compress(parent,u)
    pv = find_par_with_path_compress(parent,v)

    if pu==pv:
        return

    if rank[pu]>rank[pv]:
        parent[pv] = pu
    elif rank[pu]<rank[pv]:
        parent[pu] = pv
    else:
        parent[pv] = pu
        rank[pu] += 1

    return

def union_by_size(u,v,parent,size):
    pu = find_par_with_path_compress(parent,u)
    pv = find_par_with_path_compress(parent,v)

    if pu==pv:
        return

    if size[pu]>size[pv]:
        parent[pv] = pu
        size[pu] += size[pv] 
    elif size[pu]<size[pv]:
        parent[pu] = pv
        size[pv] += size[pu]
    else:
        parent[pu] = pv
        size[pv] += size[pu]

    return

def run_the_baby(edges,n):
    parent,rank = disjoint_set(n)
    for u,v in edges:
        union_by_rank(u,v,parent,rank)
    if find_par(parent,3)==find_par(parent,7):
        return True
    return False

edges = [[1,2],[2,3],[4,5],[6,7],[5,6],[3,7]]
print(run_the_baby(edges,7))
def disjoint(n):
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

def initial_union(parent,rank,u,v):
    pu = find_par(parent,u)
    pv = find_par(parent,v)

    if pu==pv:
        return
    if rank[pu]<rank[pv]:
        parent[pu]=pv
    elif rank[pv]<rank[pu]:
        parent[pv]=pu
    else:
        parent[pu]=pv
        rank[pv]+=1

def merge_accounts(accounts):
    
    

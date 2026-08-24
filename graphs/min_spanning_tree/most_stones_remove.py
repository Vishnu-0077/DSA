def disjoint_sets(stones):
    max_row = 0
    max_column = 0
    for x in stones:
        max_row = max(max_row,x[0])
        max_column = max(max_column,x[1])

    parent = []
    for i in range(max_row+max_column+2):
        parent.append(i)
    rank = [0]*(max_row+max_column+2)
    return max_row+1,parent,rank

def find_par(parent,i):
    if parent[i]==i:
        return i
    parent[i] = find_par(parent,parent[i])
    return parent[i]

def union_by_rank(parent,rank,u,v):
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
    return

def remove_stones(stones,n):
    max_row,parent,rank = disjoint_sets(stones)
    in_prob = []
    for u,v in stones:
        v=max_row+v
        in_prob.append(u)
        in_prob.append(v)
        union_by_rank(parent,rank,u,v)

    c=0
    for i in range(len(parent)):
        if i in in_prob and i==find_par(parent,i):
            c+=1
    return n-c

stones = [[0, 0],[ 0, 1], [1, 0],[1, 2],[2, 1],[2, 2]]
n=6
print(remove_stones(stones,n))

    

def djs(m,n):
    parent = []
    for i in range(m*n):
        parent.append(i)
    rank = [0]*(m*n)
    return parent,rank

def find_par(parent,i):
    if parent[i] == i:
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
def no_islands(n,m,k,a):
    parent,rank = djs(n,m)
    visited = []
    ans = []
    for x,y in a:
        node = x*n+y
        if node in visited:
            continue
        visited.append(node)
        for way in [[1,0],[-1,0],[0,1],[0,-1]]:
            i,j = way[0],way[1]
            xn,yn = x+i,y+j
            if 0<=xn<n and 0<=yn<m and (xn*n+yn) in visited:
                union_by_rank(parent,rank,node,xn*n+yn)
        c=0
        for i in range(n*m):
            if i in visited and find_par(parent,i) == i:
                c+=1
        ans.append(c)
    return ans


n=4
m=5
k=4
a = [[1,1],[0,1],[3,3],[3,4]] 

print(no_islands(n,m,k,a))
    

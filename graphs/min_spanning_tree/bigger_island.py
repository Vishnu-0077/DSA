def djs(grid):
    n = len(grid)
    parent = []
    for i in range(n*n):
        parent.append(i)
    rank = [0]*(n*n)
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

def bigger_island(grid):
    parent,rank = djs(grid)
    n = len(grid) #first have to connect them.....
    for x in range(n):
        for y in range(n):
            if grid[x][y] == 0:
                continue
            node = x*n+y
            for way in [[1,0],[-1,0],[0,1],[0,-1]]:
                i,j = way[0],way[1]
                xn,yn = x+i,y+j
                if 0<=xn<n and 0<=yn<n and grid[xn][yn]==1:
                    union_by_rank(parent,rank,node,xn*n+yn)
    return parent

def max_size(x,parent):
    c=0
    for i in parent:
        if i==x:
            c+=1
    return c

def mutation_section(grid):
    maxi = 0
    parent = bigger_island(grid)
    n = len(grid)
    for x in range(len(grid)):
        for  y in range(len(grid)):
            c=0
            if grid[x][y] == 1:
                continue
            for way in [[-1,0],[1,0],[0,-1],[0,1]]:
                i,j = way[0],way[1]
                xn,yn = x+i,y+j
                if 0<=xn<n and 0<=yn<n and grid[xn][yn]==1:
                    par = parent[xn*n+y]
                    c+=max_size(par,parent)
            maxi = max(maxi,c+1)
    return maxi

grid = [[1,0], [0,1]] 
print(mutation_section(grid))


            

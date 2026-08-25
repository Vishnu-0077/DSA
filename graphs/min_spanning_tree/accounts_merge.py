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

def merge_accounts(accounts):
    parent = {}
    rank = {}
    raw_accounts = accounts.copy()
    for i in range(len(accounts)):
        accounts[i][0] = i
    for x in accounts:
        parent[x[0]] = x[0]
        rank[x[0]] = 0
        for i in range(1,len(x)):
            if x[i] not in parent:
                parent[x[i]] = x[0]
                rank[x[i]] = 0
            else: #this is the main part of the code
                union_by_rank(parent,rank,x[0],find_par(parent,x[i]))
    majha_parent = []
    for i in parent:
        if parent[i]==i:
            majha_parent.append([raw_accounts[i][0],i])

    dup_dic = {}
    for i in parent:
        for x in majha_parent:
            if parent[i]==x[1]:
                if x[0] in dup_dic:
                    dup_dic[x[0]].append(i)
                else:
                    dup_dic[x[0]] = [i]

    return dup_dic

#formatting i dont know paaaa.....

accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],
["John","johnsmith@mail.com","john00@mail.com"],
["Mary","mary@mail.com"],
["John","johnnybravo@mail.com"]]
print(merge_accounts(accounts))
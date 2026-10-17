def slid(s):
    last_visited = set()
    c = 0
    l = 0
    r = 0
    max_c = 0
    while r<len(s):
        if s[r] not in last_visited:
            c+=1
            last_visited.add(s[r])
            r+=1

        else:
            last_visited.remove(s[l])
            c-=1
            l+=1
        max_c = max(c,max_c)
    return max_c

s = 'abc'
print(slid(s))

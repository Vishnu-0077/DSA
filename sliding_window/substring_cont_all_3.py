def min_window(s):
    hash = {}
    sin = set(s)
    c = 0
    for i in range(len(s)):
        hash[s[i]]=i
        if len(sin)==len(hash):
            c+=(min(hash.values())+1)
    return c    
        
s = 'bbacba'
print(min_window(s))

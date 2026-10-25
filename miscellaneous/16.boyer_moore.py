def boyer(m,s):
    hash = {'*':len(set(s))}
    for i in range(len(s)):
        hash[s[i]] = max(1,len(s)-i-1)
    i = len(s)-1
    while i<len(m):
        k = len(s)-1
        j=i
        while k>=0 and s[k]==m[j]:
            k-=1
            j-=1
        if k<0:
            return j+1
        if m[i] in hash:
            i+=hash[m[i]]
            continue
        i+=hash['*'] 

    return -1
m = 'this is a test'
s = 'test'
print(boyer(m,s))
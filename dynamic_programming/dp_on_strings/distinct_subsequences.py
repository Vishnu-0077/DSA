def rec(s,t,i,j,carry):
    if carry==t:
        return 1
    if i==len(s) or j==len(t):
        return 0
    if s[i]==t[j]:
        return rec(s,t,i+1,j+1,carry+s[i])
    return max(rec(s,t,i+1,j,carry),rec(s,t,i,j+1,carry))

s = "axbxax"
t = "axa"

print(rec(s,t,0,0,''))
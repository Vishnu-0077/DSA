def rec(str1,str2,i,j):
    if i==len(str1) or j==len(str2):
        return 0
    if str1[i]==str2[j]:
        return 1 + rec(str1,str2,i+1,j+1)
    return max(rec(str1,str2,i+1,j),rec(str1,str2,i,j+1))
#this is longest common substring formula
str1 = "flaw"
str2 = "lawn"

lcs = rec(str1,str2,0,0)
ans = (len(str1)-lcs) + (len(str2)-lcs)
print(ans)
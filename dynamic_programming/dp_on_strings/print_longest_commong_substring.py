def rec(str1,str2,i,j):
    if i==len(str1) or j==len(str2):
        return ''
    if str1[i]==str2[j]:
        return str1[i] + rec(str1,str2,i+1,j+1)
    if len(rec(str1,str2,i+1,j))>len(rec(str1,str2,i,j+1)):
        return rec(str1,str2,i+1,j)
    else:
        return rec(str1,str2,i,j+1)

str1 = "apple"
str2 = "waffle"
print(rec(str1,str2,0,0))
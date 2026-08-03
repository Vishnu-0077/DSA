def rec(str1,str2,i,j):
    if i==len(str1) or j==len(str2):
        return 0
    if str1[i]==str2[j]:
        return 1 + rec(str1,str2,i+1,j+1)
    return max(rec(str1,str2,i+1,j),rec(str1,str2,i,j+1))

str1 = 'kitten'
str2 = 'sitting'

def tablation(str1,str2):
    dp = [[0]*(len(str2)) for _ in range(len(str1))]
    for i in range(len(str1)):
        if str1[i]==str2[0]:
            dp[i][0] = 1
    for i in range(len(str2)):
        if str2[i]==str1[0]:
            dp[0][i] = 1
    for i in range(len(str1)):
        for j in range(len(str2)):
            if str1[i]==str2[j]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    return dp[len(str1)-1][len(str2)-1]
print(rec(str1,str2,0,0))
print(tablation(str1,str2))
def rec(str1,str2,i,j):
    if i==len(str1) or j==len(str2):
          return 0
    if str1[i]==str2[j]:
            if str1[i-1]==str2[j-1]:
                return 1 + rec(str1,str2,i+1,j+1)
            if i==0 or j==0:
                return 1 + rec(str1,str2,i+1,j+1)
    return max(rec(str1,str2,i+1,j),rec(str1,str2,i,j+1))

def memo(str1,str2,i,j,dp_memo):
    if i==len(str1) or j==len(str2):
          return 0
    if dp_memo[i][j]!=-1:
          return dp_memo[i][j]
    if str1[i]==str2[j]:
            if str1[i-1]==str2[j-1]:
                return 1 + memo(str1,str2,i+1,j+1,dp_memo)
            if i==0 or j==0:
                  return 1 + memo(str1,str2,i+1,j+1,dp_memo)
    dp_memo[i][j] = max(memo(str1,str2,i+1,j,dp_memo),memo(str1,str2,i,j+1,dp_memo))
    return dp_memo[i][j]

def tabulation(str1,str2):
    dp = [[0]*(len(str2)) for _ in range(len(str1))]
    for i in range(len(str1)):
        if str1[i]==str2[0]:
            dp[i][0]=1
        else:
            dp[i][0]=dp[i-1][0]
    for j in range(len(str2)):
        if str2[j]==str1[0]:
            dp[0][j]=1
        else:
             dp[0][j]=dp[0][j-1]
        
    for i in range(1,len(str1)):
        for j in range(1,len(str2)):
            if str1[i]==str2[j] and str1[i-1]==str2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    return dp[len(str1)-1][len(str2)-1]
str1 = "abcde"
str2 = "abfce"

print(rec(str1,str2,0,0))
dp_memo = [[-1]*(len(str2)) for _ in range(len(str1))]
print(memo(str1,str2,0,0,dp_memo))
print(tabulation(str1,str2))
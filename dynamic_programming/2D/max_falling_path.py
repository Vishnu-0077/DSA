def own(matrix,m,n):
    if m==0:
        return matrix[0][n]
    if n==0:
        return matrix[m][0] + max(own(matrix,m-1,n),own(matrix,m-1,n+1))
    if n==len(matrix[0])-1:
        return matrix[m][n] + max(own(matrix,m-1,n),own(matrix,m-1,n-1))
    return matrix[m][n] + max(own(matrix,m-1,n-1),own(matrix,m-1,n),own(matrix,m-1,n+1))

def dp_memo(matrix,m,n,dp):
    if n<0 or n>=len(matrix[0]):
        return float('-inf')
    if m==0:
        dp[m][n] = matrix[0][n]
        return matrix[0][n]
    if dp[m][n]!=-1:
        return dp[m][n]
    
    dp[m][n] = matrix[m][n] + max(dp_memo(matrix,m-1,n-1,dp),dp_memo(matrix,m-1,n,dp),dp_memo(matrix,m-1,n+1,dp))
    return dp[m][n]

def dp_tabulation(matrix,m,n):
    dp = [[0]*(n+1) for _ in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i==0:
                dp[i][j] = matrix[0][j]
            elif j==0:
                dp[i][j] = matrix[i][0] + max(dp[i-1][j],dp[i-1][j+1])
            elif j==n:
                dp[i][j] = matrix[i][n] + max(dp[i-1][j-1],dp[i-1][j])
            else:
                dp[i][j] = matrix[i][j] + max(dp[i-1][j-1],dp[i-1][j],dp[i-1][j+1])
    return max(dp[m])

matrix = [[1, 2, 10, 4], [100, 3, 2, 1], [1, 1, 20, 2], [1, 2, 2, 1]]
m = len(matrix)-1
n = len(matrix[0])-1
ans = []*(n+1)
for _ in range(n+1):
    ans.append(own(matrix,m,_))
print(max(ans))

dp = [[-1]*(n+1) for _ in range(m+1)]
for _ in range(n+1):
    dp_memo(matrix,m,_,dp)
print(max(dp[m]))

print(dp_tabulation(matrix,m,n))

def own(matrix,m,n):
    if matrix[m][n] == 1:
        return 0
    if m==0 or n==0:
        return 1
    return own(matrix,m-1,n) + own(matrix,m,n-1)
def dp_memo(matrix,m,n,dp):
    if matrix[m][n] == 1:
        return 0
    if m==0 or n==0:
        return 1
    if dp[m][n]!=-1:
        return dp[m][n]

    dp[m][n] = dp_memo(matrix,m-1,n,dp) + dp_memo(matrix,m,n-1,dp)
    return dp[m][n]

def dp_tabulation(matrix,m,n):
    dp = [[-1]*(n) for _ in range(m)]
    for i in range(m):
        if matrix[i][0]==0:
            dp[i][0] = 1
        else:
            dp[i][0] = 0
    for i in range(n):
        if matrix[0][i]==0:
            dp[0][i] = 1
        else:
            dp[0][i] = 0
    
    for i in range(1,m):
        for j in range(1,n):
            if matrix[i][j]==1:
                dp[i][j] = 0
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[m-1][n-1]

    
matrix = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
m = len(matrix)-1
n = len(matrix[0])-1
print(own(matrix,m,n))
dp = [[-1]*(n+1) for _ in range(m+1)]
print(dp_memo(matrix,m,n,dp))
print(dp_tabulation(matrix,m+1,n+1))

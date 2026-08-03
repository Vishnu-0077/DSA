def own(matrix,m,n):
    if m==0 and n==0:
        return matrix[0][0]
    elif m==0:
        return matrix[m][n] + own(matrix,m,n-1)
    elif n==0:
        return matrix[m][n] + own(matrix,m-1,n)
    
    return matrix[m][n] + min(own(matrix,m-1,n),own(matrix,m,n-1))

def dp_memo(matrix,m,n,dp):
    if m==0 and n==0:
        return matrix[0][0]
    elif m==0:
        return matrix[m][n] + dp_memo(matrix,m,n-1,dp)
    elif n==0:
        return matrix[m][n] + dp_memo(matrix,m-1,n,dp)
    if dp[m][n]!=-1:
        return dp[m][n]
    
    dp[m][n] = matrix[m][n] + min(dp_memo(matrix,m-1,n,dp),dp_memo(matrix,m,n-1,dp))
    return dp[m][n]

def dp_tabulation(matrix,m,n):
    dp = [[0]*(n+1) for _ in range(m+1)]
    dp[0][0] = matrix[0][0]
    for i in range(1,m+1):
        dp[i][0] = dp[i-1][0] + matrix[i][0]
    for j in range(1,n+1):
        dp[0][j] = dp[0][j-1] + matrix[0][j]
    for i in range(1,m+1):
        for j in range(1,n+1):
            dp[i][j] = matrix[i][j] + min(dp[i-1][j],dp[i][j-1])
    return dp[m][n]
matrix = [[1,2,3],[4,5,6]]
m = len(matrix) - 1
n = len(matrix[0]) - 1
print(own(matrix,m,n))
dp = [[-1]*(n+1) for _ in range(m+1)]
print(dp_memo(matrix,m,n,dp))
print(dp_tabulation(matrix,m,n))
    
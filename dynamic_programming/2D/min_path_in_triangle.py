import time

def own(matrix,m,n):
    if m==0 and n==0:
        return matrix[0][0]
    if n==0:
        return matrix[m][n] + own(matrix,m-1,n)
    if m==n:
        return matrix[m][n] + own(matrix,m-1,n-1)
    return matrix[m][n] + min(own(matrix,m-1,n-1),own(matrix,m-1,n))

def dp_memo(matrix,m,n,dp):
    if m==0 and n==0:
        return matrix[0][0]
    if n==0:
        return matrix[m][n] + dp_memo(matrix,m-1,n,dp)
    if m==n:
        return matrix[m][n] + dp_memo(matrix,m-1,n-1,dp)
    if dp[m][n]!=-1:
        return dp[m][n]
    dp[m][n] = matrix[m][n] + min(dp_memo(matrix,m-1,n-1,dp),dp_memo(matrix,m-1,n,dp))
    return dp[m][n]

def dp_tabulation(matrix,m,n):
    dp = [[-1]*(n+1) for _ in range(m+1)]
    dp[0][0] = matrix[0][0]
    for i in range(1,m+1):
        dp[i][0] = dp[i-1][0] + matrix[i][0]
    for i in range(1,m+1):
        dp[i][i] = dp[i-1][i-1] + matrix[i][i]
    for i in range(2,m):
        for j in range(1,n):
            dp[i][j] = matrix[i][j] + min(dp[i-1][j-1],dp[i-1][j])
    return dp[m][n]

def dp_space_optimised(matrix,m,n):
    dp = [-1]*(m+1)
    for i in range(m):
        for j in range(i+1):
            dp[j] = matrix[i][j] + max(dp[j],dp[j-1])
    return dp[m]
matrix = [[1], [4, 7], [4,10, 50], [-50, 5, 6, -100]]
m = len(matrix) - 1
n = m
start1 = time.time()
print(own(matrix,m,n))
print(time.time() - start1)

start2 = time.time()
dp = [[-1]*(n+1) for _ in range(m+1)]
print(dp_memo(matrix,m,n,dp))
print(time.time() - start2)

start3 = time.time()
print(dp_tabulation(matrix,m,n))
print(time.time() - start3)

start4 = time.time()
print(dp_space_optimised(matrix,m,n))
print(time.time() - start4)
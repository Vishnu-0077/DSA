import time

def own(m,n):
    if m==1 or n==1:
        return 1
    return own(m-1,n) + own(m,n-1)

def dp_memo(m,n,dp):
    if m==1 or n==1:
        return 1
    if dp[m-1][n-1]!=-1:
        return dp[m-1][n-1]
    dp[m-1][n-1] = dp_memo(m-1,n,dp) + dp_memo(m,n-1,dp)
    return dp[m-1][n-1]

def dp_tabulation(m,n):
    dp = [[-1]*n for _ in range(m)]
    
    for i in range(m):
        dp[i][0] = 1
    for j in range(n):
        dp[0][j] = 1

    for i in range(1,m):
        for j in range(1,n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]  
    return dp[m-1][n-1]

def dp_space_optimized(m, n):
    dp = [1] * n   # first row is all 1s

    for i in range(1, m):
        for j in range(1, n):
            dp[j] = dp[j] + dp[j-1]

    return dp[n-1]





start1 = time.time()
print(own(2,4))
print(time.time() - start1)

m = 2
n = 4
time2 = time.time()
dp = [[-1]*n for _ in range(m)]
print(dp_memo(m,n,dp))
print(time.time() - time2)

time3 = time.time()
print(dp_tabulation(m,n))
print(time.time() - time3)
def tabulate(arr):
    n = len(arr)
    dp = [[0]*n for _ in range(n)]
    for i in range(1,n):
        dp[i][i] = 0
    for i in range(n-1,0,-1):
        for j in range(i+1,n):
            mini = float('inf')
            for k in range(i,j):
                steps = arr[i-1]*arr[k]*arr[j] + dp[i][k] + dp[k+1][j]
                mini = min(mini,steps)
            dp[i][j] = mini
    
    return dp[1][n-1]

print(tabulate([10, 15, 20, 25]))


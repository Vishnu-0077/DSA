def rec(arr,i,j):
    if j<i:
        return 0
    mini = float('inf')
    for k in range(i,j+1):
        cost = arr[j+1] - arr[i-1] + rec(arr,i,k-1) + rec(arr,k+1,j)
        mini = min(mini,cost)
    return mini

def tabulation(arr):
    m = len(arr) - 2
    dp = [[0]*(m+2) for _ in range(m+2)]

    for i in range(m,0,-1):
        for j in range(1,m+1):
            if j<i:
                continue
            mini = float('inf')
            for k in range(i,j+1):
                cost = arr[j+1] - arr[i-1] + dp[i][k-1] + dp[k+1][j]
                mini = min(mini,cost)
            dp[i][j] = mini
    return dp[1][m]


    


arr = [1, 3, 4, 5]
arr.insert(0,0)
arr.append(7)
arr = sorted(arr)
i=1
j=len(arr)-2
print(rec(arr,i,j))
print(tabulation(arr))

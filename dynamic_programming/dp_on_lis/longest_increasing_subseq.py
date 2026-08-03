def rec(arr,i,prev):
    if i==n:
        return 0
    pick = 0
    if prev == -1 or arr[i]>arr[prev]: #- la irundhu start panna... pick.. no_pick la big number kooda filter aaidum
        pick = 1 + rec(arr,i+1,i)
    no_pick = rec(arr,i+1,prev)
    return max(pick,no_pick)

def tabulation(arr):
    n = len(arr)
    dp = [[0]*(n+1) for _ in range(n+1)]
    for i in range(n-1,-1,-1):
        for j in range(i-1,-2,-1):
            pick = 0
            if j==-1 or arr[i]>arr[j]:
                pick = 1 + dp[i+1][i+1]
            no_pick = dp[i+1][j+1]
            dp[i][j+1] = max(pick,no_pick)
    return dp[0][0]

arr = [10, 9, 2, 5, 3, 7, 101, 18]
n = len(arr)
print(rec(arr,0,-1))
print(tabulation(arr))



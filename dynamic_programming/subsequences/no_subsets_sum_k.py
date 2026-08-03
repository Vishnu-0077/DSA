def rec(arr,i,target):
    if target == 0:
        return 1
    if i==len(arr):
        return 0
    pick = 0
    if target>=arr[i]:
        pick = rec(arr,i+1,target-arr[i]) #here do addition, because, we wanna take all the paths if something is there or not
    no_pick = rec(arr,i+1,target)
    return pick+no_pick

def memo(arr,i,target,dp_memo):
    if target == 0:
        return 1
    if i==len(arr):
        return 0
    if dp_memo[i][target]!=-1:
        return dp_memo[i][target]
    pick = 0
    if target>=arr[i]:
        pick = memo(arr,i+1,target-arr[i],dp_memo)
    no_pick = memo(arr,i+1,target,dp_memo)
    dp_memo[i][target] = pick+no_pick
    return dp_memo[i][target]

def full_dp(arr,target):
    n = len(arr)
    dp = [[0]*(target+1) for _ in range(n)]
    for i in range(n):
        dp[i][0] = 1
    for i in range(1,target+1):
        if arr[0]==i:
            dp[0][arr[0]] = 1
    for i in range(1,n):
        for j in range(1,target+1):
            if j>=arr[i]:
                pick = dp[i-1][j-arr[i]]
            else:
                pick=0
            no_pick = dp[i-1][j]
            dp[i][j] = pick+no_pick
    return dp[n-1][target]

arr = [1, 2, 3, 4, 5]
target = 5
print(rec(arr,0,target))
dp_memo = [[-1]*(target+1) for _ in range(len(arr))]
print(memo(arr,0,target,dp_memo))
print(full_dp(arr,target))
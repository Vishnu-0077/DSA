def rec(arr,i,target):
    if i>=len(arr):
        return 0
    if target==0:
        return 0
    pick = 0
    if target>=arr[i]:
        pick = arr[i] + rec(arr,i+1,target-arr[i])
    no_pick = rec(arr,i+1,target)
    return max(pick,no_pick)

def memo(arr,i,target,dp_arr):
    if i>=len(arr):
        return 0
    if target==0:
        return 0
    if dp_arr[i][target]!=-1:
        return dp_arr[i][target]
    pick = 0
    if target>=arr[i]:
        pick = arr[i] + memo(arr,i+1,target-arr[i],dp_arr)
    no_pick = memo(arr,i+1,target,dp_arr)
    dp_arr[i][target] = max(pick,no_pick)
    return dp_arr[i][target]

def full_dp(arr):
    n = len(arr)
    target = sum(arr)//2
    dp = [[-1]*(target+1) for _ in range(len(arr))]
    for i in range(n): #along the y_axix where target(x = 0) is 0
        dp[i][0] = 0
    for i in range(1,target+1): #along the x_axis where the target(y=0) is 0
        if arr[0]<=i:
            dp[0][i] = arr[0]
        else:
            dp[0][i] = 0
    for i in range(1,n):
        for j in range(1,target+1):
            if j>=arr[i] and dp[i][j]!=-1:
                pick = arr[i] + dp[i-1][j-arr[i]]
            else:
                pick = 0
            no_pick = dp[i-1][j]
            dp[i][j] = max(pick,no_pick)
    return dp[n-1][target]
arr = [8, 6, 5]
print(sum(arr) - 2*rec(arr,0,sum(arr)//2))
dp_arr = [[-1]*(sum(arr)//2+1) for _ in range(len(arr))]
print(sum(arr) - 2*memo(arr,0,sum(arr)//2,dp_arr)) 
print(sum(arr) - 2*full_dp(arr))
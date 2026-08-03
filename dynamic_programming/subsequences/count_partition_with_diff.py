def rec(arr,i,target):
    if target == 0:
        return 1
    if i==len(arr):
        return 0
    if target>=2*arr[i]:
        pick = rec(arr,i+1,target-2*arr[i])
    else:
        pick = 0
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
    if target>=2*arr[i]:
        pick = memo(arr,i+1,target-2*arr[i],dp_memo)
    no_pick = memo(arr,i+1,target,dp_memo)
    dp_memo[i][target] = pick+no_pick
    return dp_memo[i][target]

def tabulation(arr):
    n = len(arr)
    dp = [[0]*(target+1) for _ in range(n)]
    for i in range(n):
        dp[i][0] = 1 #base case from recursion
    if 2*arr[0]<=target:
        dp[0][2*arr[0]] = 1 #normal...
    for i in range(1,n):
        for j in range(1,target+1): #remaining copy
            if j>=2*arr[i]:
                pick = dp[i-1][j-2*arr[i]]
            else:
                pick = 0
            no_pick = dp[i-1][j]
            dp[i][j] = pick+no_pick
    return dp[n-1][target]

arr = [1, 1, 2, 3]
diff = 1
target = (sum(arr)-diff)
print(rec(arr,0,target))
dp_memo = [[-1]*(target+1) for _ in range(len(arr))]
print(memo(arr,0,target,dp_memo))
print(tabulation(arr))
def rec(coins,i,target):
    if target==0:
        return 0
    if i==len(coins):
        return float('inf')
    pick = float('inf')
    if target>=coins[i]:
        pick = 1 + rec(coins,i,target-coins[i])
    no_pick = rec(coins,i+1,target)
    return min(pick,no_pick)
    
def memo(coins,i,target,dp_memo): #we dont need count here.... as we use the dp prev values
    if target==0:
        return 0
    if i==len(coins):
        return float('inf')
    if dp_memo[i][target]!=-1:
        return dp_memo[i][target]
    pick = float('inf')
    if target>=coins[i]:
        pick = 1 + memo(coins,i,target-coins[i],dp_memo)
    no_pick = memo(coins,i+1,target,dp_memo)
    dp_memo[i][target] = min(pick,no_pick)
    return dp_memo[i][target]

def tabulation(coins,target):
    n = len(coins)
    dp = [[float('inf')]*(target+1) for _ in range(n)]
    for i in range(n):
        dp[i][0] = 0
    if coins[0]<=target:
        dp[0][coins[0]] = 1
    for i in range(n):
        for j in range(target+1):
            if j>=coins[i]:
                pick = 1 + dp[i][j-coins[i]]
            else:
                pick = float('inf')
            no_pick = dp[i-1][j]
            dp[i][j] = min(pick,no_pick)
    return dp[n-1][target]
coins = [1,2,5]
target = 11
print(rec(coins,0,target))
dp_memo = [[-1]*(target+1) for _ in range(len(coins))]
print(memo(coins,0,target,dp_memo))
print(tabulation(coins,target))
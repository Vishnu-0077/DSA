def rec(coins,i,target):
    if target == 0:
        return 1
    if i==len(coins):
        return 0
    pick = 0
    if target>=coins[i]:
        pick = rec(coins,i,target-coins[i])
    no_pick = rec(coins,i+1,target)
    return pick+no_pick

def memo(coins,i,target,dp_memo):
    if target ==0:
        return 1
    if i == len(coins):
        return 0
    pick = 0
    if dp_memo[i][target]!=0:
        dp_memo[i][target] = 0
    if target>=coins[i]:
        pick = rec(coins,i,target-coins[i])
    no_pick = rec(coins,i+1,target)
    dp_memo[i][target] = pick+no_pick
    return dp_memo[i][target]
def tabulation(coins,target):
    n = len(coins)
    dp = [[0]*(target+1) for _ in range(len(coins))]
    for i in range(n):
        dp[i][0] = 0
    for j in range(target+1):
        if j%coins[0]==0:
            dp[0][j] = 1
    for i in range(1,n):
        for j in range(target+1):
            if j>=coins[i]:
                pick = dp[i][j-coins[i]]
            else:
                pick = 0
            no_pick = dp[i-1][j]
            dp[i][j] = pick+no_pick
    return dp[n-1][target]
        

coins = [2, 4,10]
target = 10
print(rec(coins,0,target))
dp_memo = [[0]*(target+1) for _ in range(len(coins))]
print(memo(coins,0,target,dp_memo))
print(tabulation(coins,target))
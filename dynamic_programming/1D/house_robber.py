def own(money,n):
    if n<0:
        return 0
    if n==0:
        return money[0]
    pick = money[n] + own(money,n-2)
    no_nick = own(money,n-1)
    return max(pick,no_nick)

def dp_memo(money,n,dp):
    if n<0:
        return 0
    if n==0:
        return money[0]
    if dp[n]!=-1:
        return dp[n]
    pick = money[n] + dp_memo(money,n-2)
    no_nick = dp_memo(money,n-1)
    dp[n] = max(pick,no_nick)
    return dp[n]

def dp_tabulation(money):
    n = len(money)
    dp = [-1]*n
    dp[0] = money[0]
    dp[1] = max(money[0],money[1])
    for i in range(2,n):
        dp[i] = max(money[i]+dp[i-2], dp[i-1])
    return dp[-1]

money = [1, 5, 2, 1, 6]
n = len(money)
dp = [-1]*n

print(max(own(money[1:],n-2),own(money[:n-1],n-2)))
print(max(dp_memo(money[1:],n-2,dp),dp_memo(money[:n-1],n-2,dp),n-1))
print(max(dp_tabulation(money[1:]),dp_tabulation(money[:n-1]),n-1))
#for the house robber, we should use 2 dp arrays.... arr[1:] and arr[:-1]...
#and tack the maximum of them
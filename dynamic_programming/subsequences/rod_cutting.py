def rec(price,i,n):
    if n==0:
        return 0
    if i==len(price):
        return float('-inf')
    pick = float('-inf')
    if n>=(i+1):
        pick = price[i] + rec(price,i,n-(i+1))
    no_pick = rec(price,i+1,n)
    return max(pick,no_pick)

def memo(price,i,n,dp_memo):
    if n==0:
        return 0
    if i==len(price):
        return float('-inf')
    if dp_memo[i][n]!=-1:
        return dp_memo[i][n]
    pick = float('-inf')
    if n>=(i+1):
        pick = price[i] + memo(price,i,n-(i+1),dp_memo)
    no_pick = memo(price,i+1,n,dp_memo)
    dp_memo[i][n] = max(pick,no_pick)
    return dp_memo[i][n]

price = [1, 6, 8, 9, 10, 19, 7, 20]
n = 8
print(rec(price,0,n))
dp_memo = [[-1]*(n+1) for _ in range(len(price))]
print(memo(price,0,n,dp_memo))
def rec(arr,i,state,fee): #0 means we are in state to buy
    if i==len(arr):
        return 0
    if state==0:
        we_buy = -arr[i]  + rec(arr,i+1,1,fee) #1 means we are in state to sell
        return max(we_buy,rec(arr,i+1,0,fee))
    elif state==1:
        we_sell = arr[i] -fee + rec(arr,i+1,0,fee)
        return max(we_sell,rec(arr,i+1,1,fee))
    
def memo(arr,i,state,dp_memo,fee):
    if i==len(arr):
        return 0
    if dp_memo[i][state]!=-1:
        return dp_memo[i][state]
    if state==0:
        we_buy = -arr[i] + memo(arr,i+1,1,dp_memo,fee)
        dp_memo[i][state] = max(we_buy,memo(arr,i+1,0,dp_memo,fee))
        return dp_memo[i][state]
    elif state==1:
        we_sell = arr[i] -fee + memo(arr,i+1,0,dp_memo,fee)
        dp_memo[i][state] = max(we_sell,memo(arr,i+1,1,dp_memo,fee))
        return dp_memo[i][state]
    
def tabulation(arr,fee):
    n = len(arr)

    dp = [[0]*2 for _ in range(n+1)]

    for i in range(n-1,-1,-1):
        dp[i][0] = max(
            -arr[i] + dp[i+1][1],
            dp[i+1][0]
        )

        dp[i][1] = max(
            arr[i] -fee + dp[i+1][0],
            dp[i+1][1]
        )

    return dp[0][0] # i dont know for stocks alone we run reverse tabulation
            
arr = [1, 3, 2, 8, 4, 9]
print(rec(arr,0,0,2))
dp_memo = [[-1]*2 for _ in range(len(arr))]
print(memo(arr,0,0,dp_memo,2))
print(tabulation(arr,2))
    
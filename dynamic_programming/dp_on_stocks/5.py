def rec(arr,i,state):
    if i>=len(arr):
        return 0
    if state==0:
        we_buy = -arr[i] + rec(arr,i+1,1)
        return max(we_buy,rec(arr,i+1,0))
    elif state==1:
        we_sell = arr[i] + rec(arr,i+2,0)
        return max(we_sell,rec(arr,i+1,1))

def memo(arr,i,state,dp_memo):
    if i>=len(arr):
        return 0
    if dp_memo[i][state]!=-1:
        return dp_memo[i][state]
    if state==0:
        we_buy = -arr[i] + memo(arr,i+1,1,dp_memo)
        dp_memo[i][state] = max(we_buy,memo(arr,i+1,0,dp_memo))
        return dp_memo[i][state]
    elif state==1:
        we_sell = arr[i] + memo(arr,i+2,0,dp_memo)
        dp_memo[i][state] = max(we_sell,memo(arr,i+1,1,dp_memo))
        return dp_memo[i][state]
    
def tabulation(arr):
    n = len(arr)
    dp = [[0]*2 for _ in range(n+2)]
    for i in range(n-1,-1,-1):
        for j in range(2):
            if j==0:
                we_buy = -arr[i] + dp[i+1][1]
                dp[i][j] =  max(we_buy,dp[i+1][0])
            elif j==1:
                we_sell = arr[i] + dp[i+2][0]
                dp[i][j] = max(we_sell,dp[i+1][1])
    return dp[0][0]

arr = [4,9, 0, 4, 10]
print(rec(arr,0,0))
dp_memo = [[-1]*2 for _ in range(len(arr))]
print(memo(arr,0,0,dp_memo))
print(tabulation(arr))
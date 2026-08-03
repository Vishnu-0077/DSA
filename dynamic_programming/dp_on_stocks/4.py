#same as 3rd one, just change the 2---> k... and mutate from reverse

def rec(arr,i,state,k):
    if k==0:
        return 0
    if i==len(arr):
        return 0
    if state==0:
        we_buy = -arr[i] + rec(arr,i+1,1,k)
        return max(we_buy,rec(arr,i+1,0,k))
    elif state==1:
        we_sell = arr[i] + rec(arr,i+1,0,k-1)
        return max(we_sell,rec(arr,i+1,1,k))

#change tabulation accordingly......
def tabulation(arr,k):
    n = len(arr)
    dp = [[[0]*3 for _ in range(2)] for _ in range(n+1)]
    for i in range(n-1,-1,-1):   
        for state in range(2):
            for j in range(k):
                if k==0:
                    dp[i][state][j] = 0
                else:
                    if state==0:
                        we_buy = -arr[i] + dp[i+1][1][j]
                        dp[i][state][j] = max(we_buy,dp[i+1][0][j])
                    elif state==1:
                        we_sell = arr[i] + dp[i+1][0][k-1]
                        dp[i][state][j] = max(we_sell,dp[i+1][1][j])
    return dp[0][0][k-1]


arr = [1,2,3,4,5]
k = 2
print(rec(arr,0,0,k))
print(tabulation(arr,k))

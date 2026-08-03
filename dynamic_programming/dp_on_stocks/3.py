#3 is similar to the first, just have a count array, which counts number of transactions made
#and finiish... it, how will it be for tabulation??

def rec(arr,i,state,count):
    if count==2:
        return 0
    if i==len(arr):
        return 0
    if state==0:
        we_buy = -arr[i] + rec(arr,i+1,1,count)
        return max(we_buy,rec(arr,i+1,0,count))
    elif state==1:
        we_sell = arr[i] + rec(arr,i+1,0,count+1)
        return max(we_sell,rec(arr,i+1,1,count))
def memo(arr,i,state,count,dp_memo):
    if count==2:
        return 0
    if i==len(arr):
        return 0
    if dp_memo[i][state][count]!=-1:
        return dp_memo[i][state][count]
    if state==0:
        we_buy = -arr[i] + memo(arr,i+1,1,count,dp_memo)
        dp_memo[i][state][count] = max(we_buy,memo(arr,i+1,0,count,dp_memo))
        return dp_memo[i][state][count]
    elif state==1:
        we_sell = arr[i] + memo(arr,i+1,0,count+1,dp_memo)
        dp_memo[i][state][count] = max(we_sell,memo(arr,i+1,1,count,dp_memo))
        return dp_memo[i][state][count]

def tabulation(arr):
    n = len(arr)
    dp = [[[0]*3 for _ in range(2)] for _ in range(n+1)]
    for i in range(n-1,-1,-1):   
        for state in range(2):
            for count in range(3):
                if count==2:
                    dp[i][state][count] = 0
                else:
                    if state==0:
                        we_buy = -arr[i] + dp[i+1][1][count]
                        dp[i][state][count] = max(we_buy,dp[i+1][0][count])
                    elif state==1:
                        we_sell = arr[i] + dp[i+1][0][count+1]
                        dp[i][state][count] = max(we_sell,dp[i+1][1][count])
    return dp[0][0][0]
            


arr = [3, 3, 5, 0, 0, 1, 4]
print(rec(arr,0,0,0))
dp_memo = [[[-1]*3 for _ in range(2)] for _ in range(len(arr))]
print(memo(arr,0,0,0,dp_memo))
print(tabulation(arr))
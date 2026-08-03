import time

def own(height,i,k):
    if i<=0:
        return 0
    if i==1:
        return abs(height[1]-height[0])
    mini = float('inf')
    for j in range(1,k+1):
        if i>=j:
            mini = min(mini,abs(height[i]-height[i-j])+own(height,i-j,k))
    return mini
def dp_memo(height,i,k,dp):
    if i<=0:
        return 0
    if i==1:
        return abs(height[1]-height[0])
    if dp[i]!=-1:
        return dp[i]
    mini = float('inf')
    for j in range(1,k+1):
        if i>=j:
            mini = min(mini,abs(height[i]-height[i-j])+dp_memo(height,i-j,k,dp))
    dp[i] = mini
    return mini
def dp_tabulation(height,k):
    n = len(height)
    dp = [-1]*n
    dp[0] = 0
    dp[1] = abs(height[1]-height[0])
    for i in range(2,n):
        mini = float('inf')
        for j in range(1,k+1):
            if i>=j:
                mini = min(mini,abs(height[i]-height[i-j])+dp[i-j])
        dp[i] = mini
    return dp[n-1]
    
height = [10, 5, 20, 0, 15]
k=2
i = len(height) - 1
time1 = time.time()
print(own(height,i,k))
print(time.time()-time1)

time2 = time.time()
dp = [-1]*(i+1)
print(dp_memo(height,i,k,dp))
print(time.time()-time2)

time3 = time.time()
print(dp_tabulation(height,k))
print(time.time()-time3)


import time

def own(height,i):
    if i==0:
        return 0
    if i==1:
        return abs(height[1]-height[0])
    diff_one = abs(height[i]-height[i-1])
    diff_two = abs(height[i]-height[i-2])
    one_step = diff_one+own(height,i-1)
    two_step = diff_two+own(height,i-2) #actually all can be written in same line, it will be a ultra very similar to the fibo one
    return min(one_step,two_step)

def dp_memo(height,i,dp):
    if i==0:
        return 0
    if i==1:
        return abs(height[1]-height[0])
    if dp[i]!=-1:
        return dp[i]
    diff_one = abs(height[i]-height[i-1])
    diff_two = abs(height[i]-height[i-2])
    dp[i] = min(diff_one+dp_memo(height,i-1,dp),diff_two+dp_memo(height,i-2,dp)) #here little bit i wrote on the same line
    return dp[i]

def dp_tabulation(height,k):
    n = len(height)
    dp = [-1]*n
    dp[0] = 0
    dp[1] = abs(height[1] - height[0])
    for i in range(2,n):
        dp[i] = min(dp[i-1]+abs(height[i-1]-height[i]),dp[i-2]+abs(height[i-2]-height[i])) #here i wrote in the same sentence instead of splitting
    return dp[k] #here fully i wrote on the same line

def space_optimised(heights):
    n = len(heights)
    if n == 1:
        return 0
    if n == 2:
        return abs(heights[1] - heights[0])
    prev2 = 0
    prev = abs(heights[1]-heights[0])
    for i in range(2,n):
        curr = min(prev+abs(heights[i-1]-heights[i]),prev2+abs(heights[i-2]-heights[i]))
        prev2 = prev
        prev = curr
    return curr

heights = [7, 5, 1, 2, 6]
i = len(heights)-1
dp = [-1]*(i+1)
start_1 = time.time()
print(own(heights,i))
print(time.time()-start_1)

start_2 = time.time()
print(dp_memo(heights,i,dp))
print(time.time()-start_2)

start_3 = time.time()
print(dp_tabulation(heights,i))
print(time.time()-start_3)

start_4 = time.time()
print(space_optimised(heights))
print(time.time()-start_4)



def own(nums,i):
    if i==0:
        return nums[0]
    if i<0:
        return 0
    pick = nums[i] + own(nums,i-2)
    not_pick = 0 + nums[i-1]
    return max(pick,not_pick)

def dp_memo(nums,i,dp):
    if i==0:
        return nums[0]
    if i<0:
        return 0
    if dp[i]!=-1:
        return dp[i]
    pick = nums[i] + own(nums,i-2)
    not_pick = nums[i-1]
    dp[i] = max(pick,not_pick)
    return dp[i]

def dp_tabulation(nums):
    n = len(nums)
    dp = [-1]*n
    dp[0] = nums[0]
    dp[1] = max(nums[0],nums[1])
    for i in range(2,n):
        dp[i] = max(nums[i]+dp[i-2], dp[i-1])
    return dp[-1]

def optimization(nums):
    n = len(nums)
    if n==1:
        return nums[0]
    if n==2:
        return max(nums[0],nums[1])
    prev2 = nums[0]
    prev = max(nums[0],nums[1])
    for i in range(2,n):
        curr = max(nums[i]+prev2,prev)
        prev2 = prev
        prev = curr
    return curr



nums = [2, 1, 4, 9]
n = len(nums)
print(own(nums,n-1))
dp = [-1]*n
print(dp_memo(nums,n-1,dp))
print(dp_tabulation(nums))
print(optimization(nums))
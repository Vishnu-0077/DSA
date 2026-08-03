def rec(arr,target):
    if arr == []:
        return [[]]
    first = arr[0]
    without_first = rec(arr[1:],target)
    with_first = [[first]+x for x in without_first]
    return with_first+without_first
#this gives the full subsequent list and can be found

def picknopick(arr,target):
    if target==0:
        return True
    if target<0:
        return False
    if len(arr)==0:
        return False
    pick = False
    if target>=arr[0]:
        pick = picknopick(arr[1:],target - arr[0])
    no_pick = picknopick(arr[1:],target)

    return pick or no_pick

def memo(arr,i,target,dp_memo):
    if target == 0:
        return True
    if i==len(arr):
        return False
    if dp_memo[i][target]!=-1:
        return dp_memo[i][target]
    pick = False
    if target>=arr[i]:
        pick = memo(arr,i+1,target-arr[i],dp_memo)
    no_pick = memo(arr,i+1,target,dp_memo)
    dp_memo[i][target] = pick or no_pick
    return dp_memo[i][target]

#this is saying that there will be a reverse...dp_memo arr is a solution arr...
# saying what will the answer be in the target was and n... no of elements utilized was.
# final ans dp_memo[0][target].... ans when there was n elements(0 was utilized) in arr and target was at required 

def full_dp(arr,target):
    dp = [[False]*(target+1) for _ in range(len(arr))]
    for i in range(len(arr)):
        dp[i][0] = True
    if arr[0]<=target: #when only one element...... if that first element is less than target
        dp[0][arr[0]] = True#then the corresponding dp is 0
    
    for i in range(1,len(arr)):
        for j in range(1,target+1):
            if j>arr[i]:
                pick = dp[i-1][j-arr[i]] #depends of that position
            else:
                pick = False
            no_pick = dp[i-1][j]
            dp[i][j] = pick or no_pick
    return dp[len(arr)-1][target]
    

arr = [4, 3, 5, 2]
target = 6
print(rec(arr,target))
print(picknopick(arr,target))
dp_memo = [[-1]*(target+1) for _ in range(len(arr))]
print(memo(arr,0,target,dp_memo))
print(full_dp(arr,target))
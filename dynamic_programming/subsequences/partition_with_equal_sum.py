#create all the subsetquent possibilities... and their sum should be halff of (full arr) sum
#equal sum, so 2 halfs will be made, so if anyone's sum is half of original's sum. then super

def brute(arr):
    def rec(arr):
        if arr==[]:
            return [[]]
        without_first = rec(arr[1:])
        with_first = [[arr[0]]+x for x in without_first]
        return with_first+without_first
    subsets = rec(arr)
    for p in subsets:
        if sum(p)==sum(arr)//2:
            return True
    return False

def rec(arr,i,summ):
    if summ==sum(arr)//2:
        return True
    if i>=len(arr):
        return False
    pick = False
    if (summ-sum(arr)//2)>=arr[i]:
        pick = rec(arr,i+1,summ-arr[i])
    no_pick = rec(arr,i+1,summ)
    return pick or no_pick

def memo(arr,i,summ,dp_memo):
    if summ==sum(arr)//2:
        return True
    if i>=len(arr):
        return False
    if dp_memo[i][summ]!=-1:
        return dp_memo[i][summ]
    if (summ-sum(arr)//2)>=arr[i]:
        pick = memo(arr,i+1,summ-arr[i],dp_memo)
    else:
        pick = False
    no_pick = memo(arr,i+1,summ,dp_memo)
    dp_memo[i][summ] = pick or no_pick
    return dp_memo[i][summ]

def full_dp(arr):
    n = len(arr)
    target = sum(arr)//2
    dp = [[False]*(target+1) for _ in range(len(arr))]
    for i in range(n):
        dp[i][target//2] = True
    if arr[0]<=target:
        dp[0][arr[0]] = True
    for i in range(n):
        for j in range(1,target+1):
            if j>=arr[i]:
                pick = dp[i-1][j-arr[i]]
            else:
                pick = False
            no_pick = dp[i-1][j]
            dp[i][j] = pick or no_pick
    return dp[n-1][target]

arr = [2, 3, 3, 3, 4, 5]
print(brute(arr))
print(rec(arr,0,sum(arr)))
dp_memo = [[-1]*(sum(arr)+1) for _ in range(len(arr))]
print(memo(arr,0,sum(arr),dp_memo))
print(full_dp(arr))
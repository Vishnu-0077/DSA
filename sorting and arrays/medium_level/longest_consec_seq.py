def rec(nums,i,prev):
    if i==len(nums):
        return 0
    pick = 0
    if prev==-1:
        pick = 1+rec(nums,i+1,i)
    elif abs(nums[i]-nums[prev])==1:
        pick = 1 + rec(nums,i+1,i)
    no_pick = rec(nums,i+1,prev)
    return max(pick,no_pick)

nums = [100, 4, 200, 1, 3, 2]
print(rec(sorted(nums),0,-1))
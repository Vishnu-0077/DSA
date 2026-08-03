def rec(arr,i,k):
    if k==0:
        return [[]]
    if k<0:
        return []
    if i==len(arr):
        return []
    pick_stay = [[arr[i]]+subset for subset in rec(arr,i,k-arr[i])]
    no_pick = rec(arr,i+1,k)
    return pick_stay+no_pick

arr = [2,3,6,7]
target = 7
print(rec(arr,0,target))


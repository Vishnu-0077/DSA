def rec(arr,i,state,k):
    if k==0:
        return 1
    if i==len(arr):
        return 0
    no_pick = 0
    if state==0:
        no_pick = rec(arr,i+1,0,k)
    pick = rec(arr,i+1,1,k-arr[i])
    return pick+no_pick

arr = [3, 1, 2, 4]
k=6
print(rec(arr,0,0,k))

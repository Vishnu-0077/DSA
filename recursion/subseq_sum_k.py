def rec(arr,i,k):
    if k==0:
        return True
    if i==len(arr):
        return False
    pick = rec(arr,i+1,k-arr[i])
    no_pick = rec(arr,i+1,k)
    return pick or no_pick

arr = [1,2,3,9,9]
k=8
print(rec(arr,0,k))
    
def rec(arr,i,k):
    if i>len(arr):
        return []
    if k==0:
        return [[]]
    pick = []
    if k>0:
        pick = [[arr[i]]+rem for rem in rec(arr,i+1,k-1)]
    no_pick = rec(arr,i+1,k)
    return pick+no_pick

arr = [1, 2, 3, 4]
k =3
print(rec(arr,0,k))
def rec(arr,i):
    if i==len(arr):
        return [0]
    pick = [value+arr[i] for value in rec(arr,i+1)]
    no_pick = rec(arr,i+1)
    return no_pick+pick

arr = [5,2,1]
print(rec(arr,0))
    
def rec(arr,i,prev):
    if i==len(arr):
        return []
    pick = []
    if prev == -1 or arr[i]>arr[prev]:
        pick = [arr[i]] + rec(arr,i+1,i)
    no_pick = rec(arr,i+1,prev)
    if len(pick)>len(no_pick):
        return pick
    return no_pick

arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
print(rec(arr,0,-1))
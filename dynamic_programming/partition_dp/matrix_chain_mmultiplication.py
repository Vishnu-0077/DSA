def rec(arr,i,j):
    if i==j:
        return 0
    mini = float('inf')
    for k in range(i,j):
        steps = arr[i-1]*arr[k]*arr[j] + rec(arr,i,k) + rec(arr,k+1,j)
        mini = min(mini,steps)
    return mini


arr = [40, 20, 30, 10, 30]
print(rec(arr,1,len(arr)-1))
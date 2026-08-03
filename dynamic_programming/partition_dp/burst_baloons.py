def rec(arr,i,j):
    if i>j:
        return 0
    maxi = float('-inf')
    for k in range(i,j+1):
        cost = arr[i-1]*arr[k]*arr[j+1] + rec(arr,i,k-1) + rec(arr,k+1,j)
        maxi = max(maxi,cost)
    return maxi


arr = [3,1,5,8]
n = 4
arr.insert(0,1)
arr.append(1)
print(rec(arr,1,len(arr)-2))
        
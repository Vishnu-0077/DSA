def count_sort(arr):
    n = len(arr)
    ans = [0]*n
    count = [0]*(max(arr)+1)
    for i in range(n):
        count[arr[i]]+=1
    for i in range(1,len(count)):
        count[i]+=count[i-1]
    for i in range(n-1,-1,-1):
        count[arr[i]]-=1
        ans[count[arr[i]]] = arr[i]
    return ans

arr = [2,1,1,0,2,5,4,0,2,8,7,7,9,2,0,1,9]
print(count_sort(arr))

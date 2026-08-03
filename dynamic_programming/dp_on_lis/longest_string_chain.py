def tabulate(arr):
    ans = [1]*len(arr)
    arr = sorted(arr,key= lambda x:len(x))
    for i in range(1,len(arr)):
        for j in range(i):
            if arr[i][:-1] == arr[j] and ans[j]+1 > ans[i]:
                ans[i] = ans[j]+1
    return max(ans)

arr = ["dog", "dogs", "dots", "dot", "d", "do"] 
print(tabulate(arr))
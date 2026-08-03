def tabulate_1(arr):
    ans = [1]*len(arr)
    for i in range(1,len(arr)):
        for j in range(i):
            if arr[i]>arr[j]:
                ans[i] = max(ans[i],ans[j]+1)
    pp = max(ans)
    return ans.count(pp)
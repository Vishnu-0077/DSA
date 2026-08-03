def tabulate_1(arr):
    ans = [1]*len(arr)
    for i in range(1,len(arr)):
        for j in range(i):
            if arr[i]>arr[j]:
                ans[i] = max(ans[i],ans[j]+1)
    return max(ans)

def tabulate_print(arr):
    ans = [1]*len(arr)
    hash = [0]*len(arr)
    for i in range(1,len(arr)):
        hash[i] = i
        for j in range(i):
            if arr[i]>arr[j] and ans[j]+1>ans[i]:
                ans[i] = ans[j]+1
                hash[i] = j
    ind_trace = ans.index(max(ans))
    lis = []
    prev = len(arr)
    while ind_trace!=prev:
        lis.append(arr[ind_trace])
        prev = ind_trace
        ind_trace = hash[ind_trace]
    return lis[::-1]
arr = [5,4,11,1,16,8]
print(tabulate_1(arr))
print(tabulate_print(arr))

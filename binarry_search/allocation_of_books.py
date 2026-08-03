def agressive(arr,m):
    n = len(arr)
    sub = [arr]
    extra = n-m+1
    def subsets_normal(arr,sub):
        if arr == []:
            return sub
        for x in arr:
            arr_copy = arr.copy()
            arr_copy.remove(x)
            if arr_copy not in sub:
                sub.append(arr_copy)
            subsets_normal(arr_copy,sub)
        return sub
    
    def continuous_subset(arr):
        sub = []
        for i in range(1,len(arr)-1):
            hehe = [arr[:i]]+[arr[i:i+extra]]
            for j in range(m-2):
                hehe.append([arr[j+extra]])
            sub.append(hehe)
        return sub
    
    subset = continuous_subset(arr)
    return subset

arr = [25, 46, 28, 49, 24]
m = 4
print(agressive(arr,m))



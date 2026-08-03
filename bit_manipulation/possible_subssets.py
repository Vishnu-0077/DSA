def brute_force(arr,subsets):
    n=len(arr)
    if arr not in subsets:
        subsets.append(arr)
    for num in arr:
        new_arr=arr.copy()
        new_arr.remove(num)
        brute_force(new_arr, subsets)
    return subsets
def opt(arr):
    n=len(arr)
    subsets=1<<n #this is number of subsets (2 power n)
    super_set=[]
    for i in range(subsets):
        subset=[]
        for j in range(n):
            if i&(1<<j):
                subset.append(arr[j])
        super_set.append(subset)
    return super_set
print(brute_force([1,2,3],[]))
print(opt([1,2,3]))
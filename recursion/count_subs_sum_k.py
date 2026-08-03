def brute(arr,k,power_set = []):
    if arr not in power_set:
        power_set.append(arr)
    for x in arr:
        arr_copy = arr.copy()
        arr_copy.remove(x)
        brute(arr_copy,k,power_set)
    count = 0
    for x in power_set:
        if sum(x) == k:
            count+=1
    return count


arr = [4, 2, 10, 5, 1, 3]
k = 5
print(brute(arr,k))
        
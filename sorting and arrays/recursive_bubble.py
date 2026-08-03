def recursive_bubble_sort(arr,n):
    if n==1:
        return arr
    for i in range(n-1):
        if arr[i]>arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
    return recursive_bubble_sort(arr, n-1)

print(recursive_bubble_sort([64, 34, 25, 12, 22, 11, 90], len([64, 34, 25, 12, 22, 11, 90])))
# Output: [11, 12, 22, 25, 34, 64, 90]

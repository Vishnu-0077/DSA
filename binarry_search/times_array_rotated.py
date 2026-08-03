def rotated(arr):
    low = 0
    high = len(arr) - 1
    while low < high:
        if arr[low] < arr[high]:
            return low
        mid = (low + high) // 2
        if arr[mid] >= arr[low]:
            low = mid + 1
        else:
            high = mid

    return low

arr = [3,4,5,1,2]
print(rotated(arr))
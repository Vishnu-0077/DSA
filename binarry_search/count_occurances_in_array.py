def first_occurance(arr, x):
    low = 0
    high = len(arr) - 1
    ans = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > x:
            high = mid - 1
        elif arr[mid] < x:
            low = mid + 1
        else:
            ans = mid
            high = mid - 1
    return ans

def last_occurance(arr, x):
    low = 0
    high = len(arr) - 1
    ans = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > x:
            high = mid - 1
        elif arr[mid] < x:
            low = mid + 1
        else:
            ans = mid
            low = mid + 1
    return ans

arr = [1, 2, 3, 3, 3, 3, 5, 6]
x = 3

print("First Occurance:", first_occurance(arr, x))
print("Last Occurance:", last_occurance(arr, x))
print("Count of Occurances:", last_occurance(arr, x) - first_occurance(arr, x) + 1)
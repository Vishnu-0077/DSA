def my_method(n,array,x):
    for i in range(n):
        if array[i]>=x:
            return i
    return -1

print()

def lower_bound(n,array,x):
    low = 0
    high = n - 1
    ans = -1
    while low <= high:
        mid = (low + high) // 2
        if array[mid] >= x:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans

print(lower_bound(5,[1,2,3,4,6],7))
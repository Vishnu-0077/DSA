def move_zeros(arr):
    n = len(arr)
    for i in range(n):
        if arr[i] == 0:
            arr.pop(i)
            arr.append(0)
    return arr

print(move_zeros([0, 1, 0, 3, 12]))  # Output: [1, 3, 12, 0, 0]
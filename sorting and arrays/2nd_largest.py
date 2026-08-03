def sol(arr):
    arr.sort()
    return arr[-2]


arr = [64, 25, 12, 22, 11]
print(sol(arr))
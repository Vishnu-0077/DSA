def kadane(arr):
    max_sum = float('-inf')
    max_arr = []
    summ=0
    for x in arr:
        summ+=x
        max_arr.append(x)
        if summ<0:
            summ=0
            max_arr = []
            continue
        elif summ>0:
            max_sum=max(max_sum,summ)
    while max_arr[-1]<0:
        max_arr.pop()
    return max_sum, max_arr

arr = [2, 3, 5, -2, 7, -4]
print(kadane(arr))
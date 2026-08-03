def ans(arr):
    count = 0
    for i in range(len(arr)):
        summ = 0
        for j in range(i,len(arr)):
            summ+=arr[j]
            if summ==0:
                if j-i>count:
                    count = j-i+1
    return count

arr = [6, -2, 2, -8, 1, 7, 4, -10]
print(ans(arr))
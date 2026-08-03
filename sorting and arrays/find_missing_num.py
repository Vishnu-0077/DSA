def normal(arr):
    n = len(arr)
    for i in range(1,n+2):
        if i not in arr:
            return i

def sum_of_num(arr):
    n = len(arr)+1
    summ = n*(n+1)/2
    arr_sum = sum(arr)
    return int(summ-arr_sum)

def xor(arr):
    n = len(arr)+1
    xor1=0
    xor2=0

    for i in range(n-1):
        xor1^=arr[i]
    for i in range(1,n+1):
        xor2^=i
    
    return xor1^xor2


arr = [1,2,3,4,5,7,8,9]
print(normal(arr))
print(sum_of_num(arr))
print(xor(arr))

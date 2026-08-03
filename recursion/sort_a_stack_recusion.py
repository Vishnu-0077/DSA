def func(arr):
    if len(arr)==1:
        return arr
    arr[0]=min(arr)
    return func(arr[1:]) + [arr[0]]

#yes the code is working, but now we are bound to find a way to do without using minimum

def minimum(arr,n):
    if n==1:
        return arr[0]
    elif arr[0]>=arr[1]:
        arr_new=arr[1:]
    else:
        arr_new=[arr[0]]+arr[2:]
    return minimum(arr_new,n-1)

def func_2(arr):
    if len(arr)==1:
        return arr
    arr[0]=minimum(arr,len(arr))
    return func_2(arr[1:]) + [arr[0]]

print(func([1,2,3,4,5]))
print(func_2([1,2,3,4,5]))

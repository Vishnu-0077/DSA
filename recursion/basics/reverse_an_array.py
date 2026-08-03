def func(arr,n):
    if n==1 or n==0:
        return
    arr[n-1],arr[-n]=arr[-n],arr[n-1] #see here i have just reversed their values and then later,
    func(arr[1:n-1],n-2) #wrote the function here, write on notebook for clarification
    return arr


print(func([1,2,3,4],4))
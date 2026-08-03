def search_insert(arr,target):
    n=len(arr)
    low=0
    high=n-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]>=target: #here we are finding the number which is just highest or equal to target and so we r letting the arr[mid] in the front
            ans=mid
            high=mid-1
        else:
            low=mid+1
    # If the target is not found, low will be the index where it can be inserted

    return low
print(search_insert([1,3,5,6],5))  # 2
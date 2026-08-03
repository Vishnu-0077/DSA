def upper_bound(n,array,x):
    low=0
    high=n-1
    ans=-1

    while low<=high:
        mid=(low+high)//2
        if array[mid]<=x:
            ans=mid
            low=mid+1
        else:
            high=mid-1
    return ans
print(upper_bound(5,[1,2,3,4,5],3))  # 2

#this code is wrong
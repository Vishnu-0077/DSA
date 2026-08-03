def last_occurance_in_sorted(arr,x):
    n=len(arr)
    low=0
    high=n-1
    ans=-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]>x:
            high=mid-1
        elif arr[mid]<x:
            low=mid+1
        else:
            ans=mid
            low=mid+1
    return ans
print(last_occurance_in_sorted([1,2,3,4,5,5,5,6],5))  # 6

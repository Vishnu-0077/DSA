def binarry_search(arr,target):
    n=len(arr)
    low=0
    high=n-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            return True
        elif arr[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return False
print(binarry_search([1,2,3,4,5],6))  # True

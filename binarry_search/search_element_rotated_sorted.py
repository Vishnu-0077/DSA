def search_element_rotated_sorted(arr):
    low=0
    high=len(arr)-1
    ans=-1
    while low<=high:
        mid=(low+high)//2
        if arr[low]>=arr[mid]:
            high=mid-1
            ans=high
        elif arr[mid]>=arr[high]:
            low=mid+1
            ans=low
        else:
            ans=low
            break
    return arr[ans] if ans != -1 else -1

print('Index of target element:',search_element_rotated_sorted([4,5,6,7,0,1,2]))  # 4
            


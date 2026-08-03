def small_divisor(arr,lim):
    low=1
    high=max(arr)
    ans=0
    while low<=high:
        mid=(low+high)//2
        sum=0
        for i in range(len(arr)):
            sum += (arr[i] + mid - 1) // mid
            if sum>lim:
                break
        if sum<=lim:
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans
print(small_divisor([8,4,2,3],10))
def finding_sqr_root(n): #finding the square root of a number rounding the float ans using binary search
    low=0
    high=n
    ans=0
    while low<=high:
        mid=(low+high)//2
        if mid*mid==n:
            ans=mid
            break 
        # If mid*mid is greater than n, we need to search in the left half:
        elif mid*mid>n:
            high=mid-1
        else:
            ans=mid #here we are storing because we want to round down the ans
            low=mid+1
    return ans
print(finding_sqr_root(17))  # Output: 4
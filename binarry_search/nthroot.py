def own(n,m):
    for i in range(1,m+1):
        ans=1
        for j in range(1,n+1):
            ans=ans*i
            j=j+1
            if ans==m:
                return i
            if ans>m:
                return -1

def nth_root(n, m):
    low = 1
    high = m
    ans = 0

    while low <= high:
        mid = (low + high) // 2
        power = mid ** n

        if power == m:
            return mid
        elif power < m:
            ans = mid  # Store the last valid answer
            low = mid + 1
        else:
            high = mid - 1

    return ans
#or if u dont want to use m**n then we can directly use the method used in the first function

print(own(3,27))  # Output: 3
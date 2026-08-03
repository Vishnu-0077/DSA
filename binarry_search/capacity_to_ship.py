def brute_force(weights, days):
    i=0
    for i in range(max(weights), sum(weights)+1):
        count=1
        summ=0
        j=0
        while j<len(weights):
            summ+=weights[j]
            if summ<=i:
                j=j+1
            elif summ>i:
                count+=1
                summ=0
        if count<=days:
            break
    return i

print(brute_force([1,2,3,4,5,6,7,8,9,10], 1))  #mazz da


def capacity_to_ship(weights, days):
    low=max(weights)
    high=sum(weights)
    ans = -1
    while low<=high:
        mid=(low+high)//2
        count=1
        summ=0
        j=0
        while j<len(weights):
            summ+=weights[j]
            if summ<=mid:
                j=j+1
            elif summ>mid:
                count+=1
                summ=0
        if count>days:
            low=mid+1
        else:
            ans = mid
            high=mid-1
            
    return mid


print(capacity_to_ship([5,4,5,2,3,4,5,6], 5))  # Output: 15

            

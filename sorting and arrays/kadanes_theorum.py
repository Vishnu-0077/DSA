def max_subarray(arr):
    sum_subarray=-10
    n=len(arr)

    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if i==n-1:
                sum1= arr[i]
            else:
                subarray= arr[i:j]
                sum1=sum(subarray)
            if sum1>sum_subarray:
                sum_subarray=sum1
    return sum_subarray

#print(max_subarray([1, -2, 3, 2, -1, 2, 1, -5, 4])) #brute force approach
            
def max_subarray_kadane(arr):
    max_sum=-10
    ssum=0
    for i in range(len(arr)):
        ssum=ssum+arr[i]
        if ssum>max_sum :
            max_sum=ssum
        if ssum<0:
            ssum=0
            continue
        if ssum>0:
            continue
    return max_sum

print(max_subarray_kadane([1, -2, 3, 2, -1, 2, 1, -5, 4])) #Kadane's algorithm approach

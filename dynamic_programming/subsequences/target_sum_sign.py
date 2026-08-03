def rec(arr,i,target):
    if i==len(arr):
        if target==0:
            return 1
        return 0
    add = rec(arr,i+1,target-arr[i])
    sub = rec(arr,i+1,target+arr[i])
    return add+sub

#we will  look at how to solve tabulation and memoisation of this sum later
arr = [1,1,1,1,1]
target = 3
print(rec(arr,0,target))

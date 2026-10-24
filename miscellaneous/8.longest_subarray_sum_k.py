def sol(arr,k):
    hash = {0:-1}
    pref_sum = 0
    maxi = 0
    for i in range(len(arr)):
        pref_sum+=arr[i]
        if pref_sum - k in hash:
            maxi = max(maxi,i - hash[pref_sum-k])
        if pref_sum not in hash:
            hash[pref_sum] = i
    return maxi

def pointer(arr,k): #use this if there are no negatives
    l = 0
    r = 0
    cur = 0
    maxi = 0
    while r<len(arr):
        cur+=arr[r]
        while cur>k:
            cur-=arr[l]
            l+=1

        if cur == k:
            maxi = max(maxi,r-l+1)
        r+=1
    
    return maxi
        
arr = [2, 7, 6, 1, 4, 5]
k=14
print(sol(arr,k))
print(pointer(arr,k))
        
        
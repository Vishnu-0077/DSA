def slid(nums,k):
    l = 0
    r = 0
    max_c = 0
    c = 0
    while r<len(nums):
        if nums[r]==1:
            c+=1
            r+=1
        elif nums[r]==0:
            if k!=0:
                k-=1
                c+=1
                r+=1
            else:
                if nums[l]==1:
                    c-=1
                    l+=1
                else:
                    c-=1
                    l+=1
                    k+=1
        max_c = max(c,max_c)
    
    return max_c

nums =   [0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1]
k = 3
print(slid(nums,k))
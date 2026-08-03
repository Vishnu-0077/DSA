def brute_force_hashmap(arr):
    dictt={}
    for val in arr:
        if val not in dictt:
            dictt[val]=1
        else:
            dictt[val]+=1
    for item,value in dictt.items():
        if value==1:
            return item
        
def optimized(arr): #these this works only if others are even and this guy is odd
    ans=0
    for val in arr:
        ans^=val
    return ans


print(f"the number which is occuring only once is {brute_force_hashmap([1,2,1,3,2,5])}")
print(f"the number which is occuring only once is {optimized([1,2,1,3,2,5,5])}")
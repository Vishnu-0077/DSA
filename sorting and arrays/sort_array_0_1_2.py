#better using hashing
def sort_array_0_1_2(arr):
    count={}
    for num in arr:
        if num not in count:
            count[num]=1
        else:
            count[num]+=1
    index=0
    for i in range((count[0])):
        arr[i]=0
    for i in range((count[1])):
        arr[i+count[0]]=1
    for i in range((count[2])):
        arr[i+count[0]+count[1]]=2
    return arr

        
def sort_array_0_1_2_flagmethod(arr):
    low, mid, high = 0, 0, len(arr) - 1 #bcoz we know our array is completely unsorted so from 0-n-1 it is unsorted, we sort, then we add value for mid and high and low
# [0, 1, 2, 0, 1, 2, 0, 1, 2] only not sorted, so we just take the starting of unsorted part as mid and ending of unsorted part as high, and we add values for mid, low and sub high and we update the unsorted array
    while mid<=high:
        if arr[mid]==0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid]==1:
            mid += 1
        else: # arr[mid] == 2
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    return arr

print(sort_array_0_1_2_flagmethod([0, 1, 2, 0, 1, 2, 0, 1, 2]))

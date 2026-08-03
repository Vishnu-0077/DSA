def merge_sort(arr):
    if len(arr)<=1:
        return arr
    else:
        left_half=arr[:len(arr)//2]
        right_half=arr[len(arr)//2:]
        left_half=merge_sort(left_half)
        right_half=merge_sort(right_half)
        return merge(left_half, right_half)
def merge(left, right):
    results=[]
    left_index, right_index = 0, 0
    while left_index<len(left) and right_index<len(right):
        if left[left_index]<=right[right_index]:
            results.append(left[left_index])
            left_index+=1
        else:
            results.append(right[right_index])
            right_index+=1
    while left_index<len(left):
        results.append(left[left_index])
        left_index+=1
    while right_index<len(right):
        results.append(right[right_index])
        right_index+=1
    
    return results

print(merge_sort([1,3,2,7,8,3]))

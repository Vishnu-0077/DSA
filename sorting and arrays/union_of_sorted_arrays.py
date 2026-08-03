def merge(left,right):
    left_index = 0
    right_index = 0
    result = []
    while left_index<len(left) or left_index<len(right):
        if left_index<len(left) and right_index<len(right):
            if left[left_index]<right[right_index]:
                result.append(left[left_index])
                left_index+=1
            else:
                result.append(right[right_index])
                right_index+=1
        elif left_index<len(left):
            result.append(left[left_index])
            left_index+=1
        elif right_index<len(left):
            result.append(right[right_index])
            right_index+=1

    return set(result)

left = [1,2,3,7,7]
right = [2,3,3,4,5]
print(merge(left,right))
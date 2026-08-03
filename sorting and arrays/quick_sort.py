import random
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot=random.choice(arr)
        less_than_pivot = [x for x in arr if x < pivot] #it is making a list of elements less than the pivot
        equal_to_pivot = [x for x in arr if x == pivot]#it is making a list of elements equal to the pivot
        greater_than_pivot = [x for x in arr if x > pivot]#it is making a list of elements greater than the pivot
    
    return quick_sort(less_than_pivot) + equal_to_pivot + quick_sort(greater_than_pivot) #adding the three lists together, with the pivot in the middle, pivot is in the middle because it is the pivot, and the less than and greater than lists are sorted recursively
print(quick_sort([64, 25, 12, 22, 11]))
# Output: [11, 12, 22, 25, 64]


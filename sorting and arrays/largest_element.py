def largest_element(lst):
    max = lst[0]
    for i in range(len(lst)):
        if lst[i]>max:
            max = lst[i]
    return max

print(largest_element([1,2,3,4,5]))

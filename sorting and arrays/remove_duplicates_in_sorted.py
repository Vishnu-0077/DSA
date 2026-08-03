def remove_duplicates_in_sorted(arr):
    n=len(arr)
    i=0
    while i<n-1:
        if arr[i]==arr[i+1]:
            arr.pop(i+1)
            n=n-1
        else:
            i+=1
    return arr

print(remove_duplicates_in_sorted([1, 1, 2, 2, 3, 4, 4, 5]))  # Output: [1, 2, 3, 4, 5]
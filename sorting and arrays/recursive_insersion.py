def recursive_insertion_sort(arr, n):
    if n<=1:
        return 
    # Sort the first n-1 elements
    recursive_insertion_sort(arr, n-1)
    # Insert the last element at its correct position in the sorted array
    last = arr[n-1]
    j=n-2
    # Move elements of arr[0..n-1], that are greater than last, to one position ahead of their current position
    while j>=0 and arr[j]>last:
        arr[j+1]=arr[j]
        j=j-1
    arr[j+1]=last

arr = [64, 25, 12, 22, 11]
recursive_insertion_sort(arr, len(arr))
print(arr)

#same logic as insertion sort, but code is in  reverve, but how it occurs is same as insertion sort
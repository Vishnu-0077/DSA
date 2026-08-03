def insertion_sort(arr):
    n=len(arr)
    for i in range(1,n+1):
        j=i-1
        while j >0 and arr[j-1] > arr[j]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j=j-1
    return arr

print(insertion_sort([64, 25, 12, 22, 11]))
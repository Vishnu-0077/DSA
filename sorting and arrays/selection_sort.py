def selection_sort(arr):
    n=len(arr)
    for i in range(n):
        min=arr[i]
        min_index=i
        for j in range(i+1,n):
            if arr[j]<min:
                min=arr[j]
                min_index=j
        arr[i],arr[min_index]=min, arr[i]
    return arr

print(selection_sort([64, 25, 12, 22, 11]))
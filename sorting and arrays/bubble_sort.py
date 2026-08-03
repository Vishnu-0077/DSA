def bubble_sort(arr):
    n=len(arr)
    flag = False
    for i in range(n):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                flag = True
        if not flag:
            break
    return arr
print(bubble_sort([64, 34, 25, 12, 22, 11, 90]))
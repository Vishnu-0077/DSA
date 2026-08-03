def heapify(arr,n,i):
    left = 2*i + 1
    right = 2*i + 2
    smallest = i
    
    if left < n and arr[left] < arr[smallest]:
        smallest = left
    if right < n and arr[right] < arr[smallest]:
        smallest = right
    if smallest != i:
        arr[i] , arr[smallest] = arr[smallest] , arr[i]
        heapify(arr,n,smallest)
def min_heap(arr):
    n = len(arr)
    for i in range((n-2)//2 + 1,-1,-1):
        heapify(arr,n,i)
    return arr
def sort(arr):
    heaped = min_heap(arr)
    n = len(heaped)
    sorted_arr = []
    for i in range(n):
        sorted_arr.append(heaped[0])
        heaped[0], heaped[-1] = heaped[-1] , heaped[0]
        heaped.pop()
        heapify(arr,len(heaped),0)
    return sorted_arr




print(sort([3,2,1,5,7]))
        

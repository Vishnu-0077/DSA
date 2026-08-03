def heapify(arr, n, i):
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] < arr[smallest]:
        smallest = left
    if right < n and arr[right] < arr[smallest]:
        smallest = right

    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        heapify(arr, n, smallest)  # keep fixing downward
def build_heap(arr, n):
    for i in range((n - 2) // 2 + 1, -1, -1):
        heapify(arr, n, i)
    return arr

def kth_smallest(arr,k): #yes, this works only if the array is already heapified, so lets heapify it
    arr = build_heap(arr,len(arr))
    for i in range(k-1):
        arr[0],arr[-1] = arr[-1], arr[0] #literally we are just sorting here, if we do this the arr will get sorted, then we can apply whatever we want
        heapify(arr,len(arr)-1,0) #sorting also same
        arr.pop()
    return arr[0]
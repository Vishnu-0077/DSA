def is_min_heap(arr):
    n = len(arr)
    # Check all internal nodes
    for i in range((n - 2) // 2 + 1):  # this range value came from the formula of right
        left = 2 * i + 1
        right = 2 * i + 2
        
        # Check left child
        if left < n and arr[i] > arr[left]:
            return False
        
        # Check right child
        if right < n and arr[i] > arr[right]:
            return False
    
    return True


# Example usage
print(is_min_heap([1, 3, 5, 7, 9, 8]))  # ✅ True
print(is_min_heap([10, 15, 20, 17, 25]))  # ✅ True
print(is_min_heap([10, 9, 20]))  # ❌ False

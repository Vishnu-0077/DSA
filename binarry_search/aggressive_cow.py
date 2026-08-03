def canPlace(stalls, k, min_dist):
    """
    Checks if it's possible to place 'k' cows such that
    the minimum distance between any two is at least 'min_dist'.
    """
    cows_placed = 1
    last_placed_cow_pos = stalls[0] # Place the first cow in the first stall

    for i in range(1, len(stalls)):
        if stalls[i] - last_placed_cow_pos >= min_dist:
            cows_placed += 1
            last_placed_cow_pos = stalls[i]
        
        if cows_placed >= k:
            return True
            
    return False

def aggressiveCows(stalls, k):
    """
    Finds the maximum possible minimum distance between k aggressive cows.
    """
    n = len(stalls)
    stalls.sort() # Important: Sort the stalls first

    low = 1  # Minimum possible distance
    high = stalls[n - 1] - stalls[0]  # Maximum possible distance
    ans = 0

    while low <= high:
        mid = low + (high - low) // 2 # Calculate mid to avoid overflow for large low/high

        if canPlace(stalls, k, mid):
            ans = mid  # mid is a possible answer, try for a larger distance
            low = mid + 1
        else:
            high = mid - 1 # mid is too large, try a smaller distance
            
    return ans

# Test Cases
print(aggressiveCows([1, 2, 4, 8, 9], 3))  # Output: 3 (Cows at 1, 4, 8 -> min dist is 3)
print(aggressiveCows([10, 1, 2, 7, 5], 3)) # Output: 4 (Sorted: [1, 2, 5, 7, 10]. Cows at 1, 5, 10 -> min dist is 4)
print(aggressiveCows([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5)) # Output: 2
print(aggressiveCows([0, 3, 4, 7, 10, 9], 4)) # Output: 3 (Sorted: [0,3,4,7,9,10]. Cows at 0,3,7,10 -> min dist 3)
    


            
            


        



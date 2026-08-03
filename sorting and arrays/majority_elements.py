def majority_elements(nums): #this is done using hashing
    count={}
    n=len(nums)
    for i in range(n):
        if nums[i] not in count:
            count[nums[i]]=1
        else:
            count[nums[i]]+=1
    majority_count = n // 3

    majority_elements = []

    for i in range(n):
        if count[nums[i]] >= majority_count and  nums[i] not in majority_elements:
            majority_elements.append(nums[i])
    return majority_elements

#boyer algorithm explanation:
'''
Imagine you're voting. 
Every time you see an element that matches your current "candidate" for the majority, 
you vote for it (increment a counter). If you see an element that doesn't match your candidate, 
you vote against it (decrement the counter). If your votes for the current candidate drop to zero, 
it means that candidate is no longer a strong contender, so you pick a new candidate from the array and reset your vote count to 1

but this is valid only for finding the majority element, which is more than n/2.
For finding elements that appear more than n/3 times, we need to track the count of to condidates
'''
def find_majority_element(arr): #boyer _moore_algorithm:
    candidate = None
    count = 0

    # First pass: Find a potential candidate
    for num in arr:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1

    # Second pass: Verify if the candidate is indeed the majority element
    if candidate is not None:
      count = 0
      for num in arr:
          if num == candidate:
              count += 1
      if count > len(arr) // 2:
        return candidate
    return None


print(majority_elements([3, 2, 3,3,3,3,3,3,3]))  # Output: [3]


            

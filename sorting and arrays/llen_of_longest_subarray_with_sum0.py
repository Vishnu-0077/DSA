#brute force method is same as the brute force method of kadane's algorithm, but the difference is that we are looking for the longest subarray with sum zero instead of the maximum sum subarray.

def longest_subarray_with_sum_zero(arr):
    n = len(arr)
    max_length = 0
    sum_map = {}
    current_sum = 0

    for i in range(n):
        current_sum += arr[i]

        if current_sum == 0:
            max_length = i + 1

        if current_sum in sum_map:
            max_length = max(max_length, i - sum_map[current_sum])
        else:
            sum_map[current_sum] = i

    return max_length

def hamara(arr):
    current_sum = 0
    max_len = 0
    le = 0
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)+1):
            current_sum = sum(arr[i:j])
            if current_sum == 0:
                le = int(j-i)
                if le >= max_len:
                    max_len = le
    return max_len
            

print(longest_subarray_with_sum_zero([1, -1, 2, -2, 3, -3]))  # Output: 6
print(hamara([1, -1, 2, -2, 3, -3]))
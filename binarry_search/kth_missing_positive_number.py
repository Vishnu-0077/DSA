def brute_force(vec,k):
    n=max(vec)
    missing=[]
    for i in range(1,n+1):
        if i not in vec:
            missing.append(i)
    return missing[k-1]

print(brute_force([2,3,4,7,11], 5))  # Output: 9

def missingK(vec, n, k):
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        missing = vec[mid] - (mid + 1)
        if missing < k:
            low = mid + 1
        else:
            high = mid - 1
    return k + high + 1

vec = [4, 7, 9, 10]
n = 4
k = 4
ans = missingK(vec, n, k)
print("The missing number is:", ans)

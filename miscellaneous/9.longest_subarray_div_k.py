def hash_type(arr,k):
    maxi = 0
    pref_sum = 0
    hash = {0:-1}
    for i in range(len(arr)):
        pref_sum+=arr[i]
        rem = pref_sum % k
        if rem in hash:
            maxi = max(maxi,i - hash[rem])
        else:
            hash[rem] = i
    return maxi

arr = [2, 7, 6, 1, 4, 5]
k = 3

print(hash_type(arr,k))


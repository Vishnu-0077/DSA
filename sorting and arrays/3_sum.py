def triplet(n, arr):
    st = set()

    # check all possible triplets:
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if arr[i] + arr[j] + arr[k] == 0:
                    temp = [arr[i], arr[j], arr[k]]
                    temp.sort()
                    st.add(tuple(temp))

    # store the set elements in the answer:
    ans = [list(item) for item in st]
    return ans
#that is brute force solution with O(n^3) time complexity , 3 loops

#better solution would be use 2 loops instead of 3 and write if arr[k]

def triplet_better(n,arr):
    ans=set()
    for i in range(n):
        hashset = set()
        for j in range(i + 1, n):
            third = -(arr[i] + arr[j])
            if third in hashset:
                triplet=[arr[i], arr[j], third]
                triplet.sort()
                ans.add(tuple(triplet))
            hashset.add(arr[j])
    return list(ans)


#above is a better solution

def triplet_optimal(n, arr):
    ans = []
    arr.sort()
    for i in range(n):
        # remove duplicates:
        if i != 0 and arr[i] == arr[i - 1]:
            continue

        # moving 2 pointers:
        j = i + 1
        k = n - 1
        while j < k:
            total_sum = arr[i] + arr[j] + arr[k]
            if total_sum < 0:
                j += 1
            elif total_sum > 0:
                k -= 1
            else:
                temp = [arr[i], arr[j], arr[k]]
                ans.append(temp)
                j += 1
                k -= 1
                # skip the duplicates:
                while j < k and arr[j] == arr[j - 1]:
                    j += 1
                while j < k and arr[k] == arr[k + 1]:
                    k -= 1

    return ans
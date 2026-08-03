def tabulate_1(arr):
    ans = [1]*len(arr)
    for i in range(1,len(arr)):
        for j in range(i):
            if arr[i]>arr[j]:
                ans[i] = max(ans[i],ans[j]+1)
    return ans

arr = [5, 1, 4, 2, 3, 6, 8, 7] 
lis_forward = tabulate_1(arr)
lis_backward = tabulate_1(arr[::-1])

import numpy as np
result = np.array(lis_forward) + np.array(lis_backward) -1
print(max(result) - 1)
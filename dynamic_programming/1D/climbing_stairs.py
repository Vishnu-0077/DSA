#same as fibonocci as can climb only 1 or 2 steps at a time

def recur(n):
    if n<=0:
        return 0
    elif n==1:
        return 1
    return recur(n-1) + recur(n-2)

def rec_memo(n,dp_arr):
    if dp_arr[n]!=-1:
        return dp_arr[n]
    elif n<=0:
        return n
    elif n==1:
        return n
    dp_arr[n] = rec_memo(n-1,dp_arr) + rec_memo(n-2,dp_arr)
    return dp_arr[n]

def tabulation(n):
    dp_arr = [-1]*(n+1)
    dp_arr[0] = 0
    dp_arr[1] = 1
    for i in range(2,n+1):
        dp_arr[i] = dp_arr[i-1] + dp_arr[i-2]
    return dp_arr[n]
n = 8
dp_arr = [-1]*(n+1)
import time
start1 = time.time()
print(recur(n))
print(time.time() - start1)

start2 = time.time()
print(rec_memo(n,dp_arr))
print(time.time() - start2)

start3 = time.time()
print(tabulation(n))
print(time.time() - start3)

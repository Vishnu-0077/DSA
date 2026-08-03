import time

def normal_fibbo(n): #normal recursion..takes space and time
    if n<=0:
        return 0
    elif n==1:
        return 1
    return normal_fibbo(n-1)+normal_fibbo(n-2)
def fibbo_dp_memo(n,dp_arr): #reduced the time complexity to max, but more space
    if dp_arr[n]!=-1:
        return dp_arr[n]
    if n<=1:
        return n
    dp_arr[n] = fibbo_dp_memo(n-1,dp_arr)+fibbo_dp_memo(n-2,dp_arr)
    return dp_arr[n]
def fib_tabulation(n): #reduces the space compl to good extent
    dp_arr = [-1]*(n+1)
    dp_arr[0] = 0
    dp_arr[1] = 1
    for i in range(2,n+1):
        dp_arr[i] = dp_arr[i-1]+dp_arr[i-2]
    return dp_arr[n]

def fib_tabulation_space(n): #completely removes spacce complexity
    prev_b = 0
    prev_a = 1

    for i in range(n):
        prev_b,prev_a = prev_a,prev_a+prev_b
    return prev_b

start = time.time()
dp_arr = [-1]*(10+1)
print(fib_tabulation_space(10))
end = time.time()
print(end-start)
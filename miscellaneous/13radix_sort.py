def counting_sort(arr,exp):
    n = len(arr)
    ans = [0]*n
    count = [0]*10
    for i in range(n):
        count[(arr[i]//exp)%10]+=1 # if exp=1 -- ones is takem, if exp=10---- then ten's is taken
    for i in range(1,len(count)):
        count[i]+=count[i-1] #same as of counting_sort
    for i in range(n-1,-1,-1):
        count[(arr[i]//exp)%10]-=1
        ans[count[(arr[i]//exp)%10]] = arr[i]
    
    return ans

def radix(arr):
    maxi = max(arr)
    exp = 1
    while maxi%exp<10:
        arr = counting_sort(arr,exp)
        exp*=10
    return arr
    

arr = [170, 45, 75, 90, 802, 24, 2, 66]
print(radix(arr))


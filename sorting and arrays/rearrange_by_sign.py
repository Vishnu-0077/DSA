def ans(arr):
    ans = [0]*len(arr)
    pos = 0
    neg = 1
    for x in arr:
        if x>0:
            ans[pos]=x
            pos+=2
        else:
            ans[neg]=x
            neg+=2
    return ans

arr = [1,2,-4,-5]
print(ans(arr))


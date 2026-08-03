def brute(arr):
    c=0
    c_max=0
    for x in arr:
        if x==1:
            c+=1
        else:
            c=0
        c_max=max(c,c_max)
    return c_max

arr = [1, 1, 0, 1, 1, 1]
print(brute(arr))

def sleeping(s,n,k):
    can_sleep = 0
    slept = 0
    i = 0
    while i<n:
        if s[i] == '1':
            can_sleep = i + k + 1
            i = i+1
        elif s[i] == '0' and i >= can_sleep:
            slept = slept + 1
            i = i+1
        else:
            i = i+1
    return slept

t = int(input())
for i in range(t):
    n,k = map(int,input().split())
    s = input()
    s = str(s)
    print(sleeping(s,n,k))

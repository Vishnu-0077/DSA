#it is in fibonocci series format
#count the number of strings without the consecutive ones

def func(n):
    if n==1:
        return 2
    if n==0:
        return 1
    return func(n-1)+func(n-2)
print(func(4))

    
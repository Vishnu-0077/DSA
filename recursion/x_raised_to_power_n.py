#find x raised tto power n

def func(x,n):
    if n==0:
        return 1
    return func(x,n-1)*x
print(func(2,3))
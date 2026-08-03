def func(n):
    if n<=0:
        return 0
    elif n==1:
        return 1
    return func(n-1)+func(n-2)

for i in range(100):
    print(func(i))


'''
remember line function is mathermatics, the final return contains the output of the func, line we know for this case
next value of the finanocci term is f(n)=f(n-1)+f(n-2), so we use this in return, and the if_case return we use it for the
extreme cases or as a stop condition
'''
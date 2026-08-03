def func(s1):
    if len(s1)==0 or len(s1)==1:
        return True
    if s1[0]==s1[-1]:
        return func(s1[1:-1])
    return False
print(func('aabbaaa'))

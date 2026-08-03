#print the name n times

def func(name,n):
    if n==0:
        return
    func(name,n-1)
    print(name)
func("hello",5)

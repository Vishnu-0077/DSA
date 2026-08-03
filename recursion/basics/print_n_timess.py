def func(num,n):
    if n==0:
        return
    func(num,n-1)
    print(num)
func(3,4)
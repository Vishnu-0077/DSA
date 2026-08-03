def check_odd_eve(n):
    binary=bin(n)[2:]
    if binary[-1]=='0':
        return True
    else:
        return False
print("enter an intger")
n=int(input())

if check_odd_eve(n):
    print("even")
else:
    print("odd")
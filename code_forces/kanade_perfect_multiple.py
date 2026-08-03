def adding_divisor(n,b):
    if n == 1:
        if 1 not in b:
            b.append(1)
            return b
        else:
            return b
    
    for i in range(2,n+1):
        if n%i == 0:
            if i not in b:
                b.append(i)
                return b
            else:
                return b
        else:
            continue
def multiples(a,k,b):
    i = 1
    mul = b
    while mul<=k:
        if mul not in a:
            return False
        i+=1
        mul = b*i
    return True

def main(a,n,k,b = None):
    if b is None:
        b = []
    for i in range(n):
        b = adding_divisor(a[i],b)
    Flag = True
    for i in range(len(b)):
        if multiples(a,k,b[i]):
            continue
        else:
            Flag = False
            break
    if Flag:
        return len(b), sorted(b)
    else:
        return -1, -1

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n,k = map(int,input().split())
        a = list(map(int,input().split()))
        s,b = main(a,n,k)

        if s == -1:
            print(-1)
        else:
            print(s)
            for i in range(s-1):
                print(b[i],end=" ")
            print(b[-1])
        
    

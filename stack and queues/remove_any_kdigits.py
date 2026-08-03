#idea is get rid of first k larger digits

def own_method(s,k):
    n=len(s)
    stack=[]
    for i in range(n):
        while (stack and stack[-1]>s[i] and k!=0) or (stack and stack[-1]=='0' and k!=0):
            stack.pop()
            k-=1
        stack.append(s[i])
    return ''.join(stack[::])


s="1432219"
k=3
print(own_method(s,k))




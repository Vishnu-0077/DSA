def sol(s):
    s = s[::-1]
    stack = []
    for x in s:
        if x.isalnum():
            stack.append(x)
        else:
            l = stack.pop()
            r = stack.pop() #there is a change here... as this is prefix
            stack.append('('+l+x+r+')')
    return stack.pop()

s = "+ab"
print(sol(s))
def sol(s):
    stack = []
    for x in s:
        if x.isalnum():
            stack.append(x)
        else:
            r = stack.pop()
            l = stack.pop()
            stack.append(x+l+r)
    return stack.pop()

s = 'ab+'
print(sol(s))
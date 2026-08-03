def ans(s):
    stack = []
    for x in s:
        if x.isalnum():
            stack.append(x)
        else:
            r = stack.pop()
            l = stack.pop()
            stack.append('('+l+x+r+')')
    return stack.pop()

s = "ab+c*"
print(ans(s))

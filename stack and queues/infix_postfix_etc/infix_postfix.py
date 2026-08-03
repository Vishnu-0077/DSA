def sol(s):
    priority = {"(":0,")":0,"+":1,"-":1,"*":2,"/":2,'^':3}
    ans = ''
    stack = []
    for x in s:
        if x==' ':
            continue
        elif x.isalnum():
            ans+=x
        elif x=='(':
            stack.append(x)
        elif x==')':
            while stack and stack[-1]!='(':
                ans+=stack.pop()
            stack.pop()
        else:
            while stack and priority[x]<=priority[stack[-1]]:
                ans +=stack.pop()
            else:
                stack.append(x)
    while stack:
        ans+=stack.pop()
    return ans

s = 'a + b * (c^d - e) ^ (f + g * h) - i'
print(sol(s))
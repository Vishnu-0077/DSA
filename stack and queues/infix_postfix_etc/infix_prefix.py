def sol(s):
    priority = {"(":0,")":0,"+":1,"-":1,"*":2,"/":2,'^':3}
    ans = ''
    stack = []
    s = s[::-1]
    for i in range(len(s)):
        if s[i]=='(':
            s[i]=')'
        elif s[i]==')':
            s[i]='('
        else:
            continue
    for x in s:
        if x==' ':
            continue
        elif x.isalnum():
            ans+=x
        elif x=='(':
            stack.append(x)
        elif x==')':
            while stack[-1]!='(':
                ans+=stack.pop()
            stack.pop()
        else:
            while stack and priority[x]<priority[stack[-1]]:
                ans +=stack.pop()
            else:
                stack.append(x)
    while stack:
        ans+=stack.pop()
    return ans[::-1]

s = 'x + y * z / w + u '
print(sol(s))
def solution(s):
    while s[0]==' ':
        s = s[1:]
    if s[0]=='-':
        s = s[1:]
        sign = '-'
    elif s[0]=='+':
        s = s[1:]
        sign = '+'
    else:
        sign = '+'
    ans = ''
    while s and s[0] in '0123456789':
        ans += s[0]
        s = s[1:]
    return int(sign+ans)
    
print(solution('   -42'))
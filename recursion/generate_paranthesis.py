def paranthesis(n, m=None, paran=''):
    if m is None: #see when adding a new parameter, keeping this is m is None and assigning value is useful
        m=n
    if n == 0 and m == 0:
        print(paran)
        return
    if n != 0:
        paranthesis(n-1, m, paran+'(')
    if m != 0:
        paranthesis(n, m-1, paran+')')
    
paranthesis(3)

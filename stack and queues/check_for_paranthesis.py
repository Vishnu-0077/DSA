def check(s):
    st=[]
    for par in s:
        if par=='(' or par=='[' or par=='{':
            st.append(par)
        else:
            opp=st[-1]
            st.pop()
            if (par==')' and  opp=='(') or (par == '}' and opp == '{') or (par == ']' and opp == '['):
                continue
            else:
                return False
    return len(st)==0

if __name__ == '__main__':
    s = "()[{}()]"
    if check(s):
        print("True")
    else:
        print("False")
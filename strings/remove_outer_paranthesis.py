def brute_force(s):
    primitive_stack = []
    count=0
    stack=[]
    for char in s:
        if char=='(':
            count+=1
            stack.append(char)
        elif char==')':
            count-=1
            stack.append(char)
        if count==0 and stack is not None:
            primitive_stack.append(''.join(stack))
            count=0
            stack=[]
    final_string = ''
    for stackk in primitive_stack:
        stackk=list(stackk)
        stackk.pop(0)
        stackk.pop(-1)
        final_string = final_string+''.join(stackk)

    return final_string

print(brute_force("(()())(())"))  # Output: ()()()
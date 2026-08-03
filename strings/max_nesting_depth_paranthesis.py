def max_paranthesis_depth(s):
    max_depth=0
    current_depth = 0
    for char in s:
        if char=='(':
            current_depth= current_depth + 1
            max_depth = max(max_depth, current_depth)
        elif char==')':
            current_depth = current_depth - 1
    return max_depth

print(max_paranthesis_depth("((()))"))  # Output: 3
print(max_paranthesis_depth("(()())"))  # Output: 2
print(max_paranthesis_depth("()()"))    # Output: 1
print(max_paranthesis_depth(")("))      # Output: 0
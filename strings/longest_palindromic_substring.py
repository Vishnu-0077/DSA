def is_palindrome(s):
    if s==s[::-1]:
        return True
    return False

def power_set_gen(s):
    if len(s)==0:
        return [[]]
    first = s[0]
    rest_subset = power_set_gen(s[1:])
    with_first = [[first]+subset for subset in rest_subset]
    return with_first+rest_subset

s = 'babad'
ans = power_set_gen(s)
str_ans = []
for x in ans:
    str_ans.append(''.join(x))
print(str_ans)
print()
maxi = 0
value = 0
for sub in str_ans:
    if is_palindrome(sub):
        value = len(sub)
    maxi = max(maxi,value)

print(maxi)

    

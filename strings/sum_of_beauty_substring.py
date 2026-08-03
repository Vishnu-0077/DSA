def beauty_value(s):
    char_count = {}
    for char in s:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    return max(char_count.values()) - min(char_count.values())

def sum_of_beauty_substring(s):
    total_beauty=0
    n = len(s)
    Flag= False
    for k in range(n-1): #here can also use len(set(s)) to check if all characters are same
        if s[k]==s[k+1]:
            Flag=True
        else:
            Flag=False
            break
    if Flag==True:
        return 0
    for i in range(1,n+1):
        for j in range(n-i+1):
            sub_str=s[j:j+i]
            total_beauty += beauty_value(sub_str)
    return total_beauty

print(sum_of_beauty_substring("aaaa"))  # Output: 5
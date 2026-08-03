def brute_force(s):
    char_count={}
    for char in s:
        if char not in char_count:
            char_count[char]=1
        else:
            char_count[char]+=1
    return sorted(char_count.items(), key=lambda x: x[1], reverse=True)

print(brute_force("tree"))  # Output: [('e', 1), ('r', 1), ('t', 1)]
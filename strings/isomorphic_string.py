def hashing(s):
    char_count = {}
    for char in s:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    sorted_values=list(sorted(char_count.values()))
    return sorted_values

def isomorphic(s1,s2):
    if len(s1)!=len(s2):
        return False
    if hashing(s1)==hashing(s2):
        return True
    return False

print(isomorphic("paper","title"))  # Output: True
    
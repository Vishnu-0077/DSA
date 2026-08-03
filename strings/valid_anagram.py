def hashing(s):
    char_count = {}
    for char in s:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    sorted_one=sorted(char_count.items())
    return ''.join([f"{k}{v}" for k, v in sorted_one])

def anagram(s1,s2):
    if len(s1)!=len(s2):
        return False
    if hashing(s1)==hashing(s2):
        return True
    return False

print(anagram("anagram","nagaram"))  # Output: True
    
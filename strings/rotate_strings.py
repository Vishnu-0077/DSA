def rotate(s):
    half = len(s) // 2
    return s[half:] + s[:half]

print(rotate('rotation'))
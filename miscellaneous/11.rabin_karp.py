def hehe(text, pattern):
    n = len(text)
    m = len(pattern)
    ans = []
    for i in range(n-m+1):
        if text[i:i+m]==pattern:
            ans.append(i)
    return ans

text = 'aadkidiaddadadd'
pattern = 'add'
print(hehe(text,pattern))
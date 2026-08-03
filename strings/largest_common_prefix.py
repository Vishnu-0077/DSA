def largest_common_prefix(lst):
    prefix=[]
    Flag=False
    for i in range(len(lst[0])): # i will turn for each char
        for j in range(len(lst)-1): #j will turn for every word in lst
            if lst[j][i]==lst[j+1][i]:
                Flag=True
            else:
                Flag=False
                break
        if Flag==True:
            prefix.append(lst[0][i])
        else:
            break
    return ''.join(prefix)

print(largest_common_prefix(["flower", "flow", "flight"]))  # Output: "fl"
            
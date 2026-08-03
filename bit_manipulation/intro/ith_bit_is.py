def ith_bit_is(n,i):
    binary=bin(n)[2:]
    binary_rev=binary[::-1]
    if i>=len(binary_rev):
        return 0
    return binary_rev[i]
def ith_bit_in_binarry_method(n,i):
    if n&(1<<i)!=0:
        return 1    
    else:
        return 0
print(ith_bit_is(5,0))
print(ith_bit_in_binarry_method(5,0))

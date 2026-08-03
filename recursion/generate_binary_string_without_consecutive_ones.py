def generate_bin(n):
    if n==1:
        return ['1','0']
    one = '1'
    zero = '0'
    remaining = generate_bin(n-1)
    pick_one = [one+sub for sub in remaining if sub and sub[0]!='1']
    pick_zero = [zero+sub for sub in remaining]
    return pick_one + pick_zero

n=2
print(generate_bin(n))
    

    

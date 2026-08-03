def brute_force(s):
    while int(s[-1])%2==0:
        s=s[:-1]
    while int(s[0])==0:
        s=s[1:]
        
    return s
            

   
print(brute_force("0234567"))  # Output: "123456789"


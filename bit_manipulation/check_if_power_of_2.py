def check_if_power_of_2(n):
    binary=bin(n)[2:]
    count=-1
    for x in binary:
        if x=='1':
            count+=1
        else:
            continue
    if count==0:
        return True
    else:
        return False

print(check_if_power_of_2(8))

#logic is the binary can have only one '1' then only it is a power of 2

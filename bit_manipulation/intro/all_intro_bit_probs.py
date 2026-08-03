# add ith bit and return the resulting number (set the ith bit to 1)
'''
eg if 6 is given, binarry 0110, so if the i is 3, the it will become 0110+1000=1110,
so the final answer will be 14
'''
def add_ith_bit(n,i):
    return n | (1<<i)
print(f"the number after adding the ith bit is {add_ith_bit(6,3)}")

'''
brute force will be take the ith bit of the number and check if it is 0 or 1, if 0 then set it to 1
the change the number from binarry to num again and return the number'''

#-----------------------------------------------------------

# clear the ith bit(set it to 0)

def clear_ith_bit(n,i):
    return n & ~(1<<i)
print(f"the number after clearing the ith bit is {clear_ith_bit(6,2)}")

'''
brute force will be, find the ith bit of the number and check if it is 0 or 1, if 1 then set it to 0
the change the number from binarry to num again and return the number'''

#------------------------------------------------------------

#toogle  the ith bit

def toggle_ith_bit(n,i):
    return n ^ (1<<i)
print(f"the number after toggling the ith bit is {toggle_ith_bit(6,1)}")

#---------------------------------------------------------------------

def remove_the_last_occurance_of_set(n):
    return n & (n-1)
print(f"the number after removing the last occurance of set is {remove_the_last_occurance_of_set(6)}")

"""brute force will be use a for loop in reversed_binary and if one arrives, change it to 0 and return the number"""

#------------------------------------------------------------------

#check if a number is power of 2

def check_if_power_of_2(n):
    if n & (n-1)==0:
        return True
    else:
        return False
if check_if_power_of_2(16):
    print("yes it is a power of 2")
else:
    print("no,it is not a power of 2")

'''
same logic as before, that the number is power 2 if only one set is available, n & (n-1)==0, removes the last available set
so if that set is gone value is 0, so majha
'''

#---------------------------------------------------------------

#count the number of set bits: this shit is pure brute force, no short cut

def count_set_bits(n):
    binary=bin(n)[2:]
    count=0
    for x in binary:
        if x=='1':
            count+=1
        else:
            continue
    return count
#other wise there is an other way that if from number, convert it into bin using the paper method, and while doing that only count the number of 1's

print(f"the number of set bits is {count_set_bits(9)}")

#---------------------------------------------------------------

#count the number of set bits

def number_of_set_bits_v_2(n):
    count=0
    while n!=0:
        count+=(n&1)
        n=n>>1
    return count
print(F"the number of set bits_version_2 is {number_of_set_bits_v_2(9)}")
        
    
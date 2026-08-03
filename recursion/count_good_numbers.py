def is_prime(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True

def count_good_numbers(n):
    count=0
    for num in range(10**n):
        num_str=str(num).zfill(n) #given in question
        Flag=True
        for i in range(0,len(num_str),2):
            if int(num_str[i])%2==0:
                continue
            else:
                Flag=False
        for i in range(1,len(num_str),2):
            if not is_prime(int(num_str[i])):
                Flag=False
        if Flag:
            count+=1
    return count

def count_good_numbers_fixed_brute_force(n): #this is chat_gpt, 
    count = 0
    # Iterate through all numbers from 0 to 10^n - 1
    # For n=4, this covers 0 to 9999
    for num in range(10**n):
        # Pad with leading zeros to ensure it's always 'n' digits long
        num_str = str(num).zfill(n)
        
        Flag = True
        for i in range(n): # Iterate through all indices
            digit = int(num_str[i])
            if i % 2 == 0:  # Even index
                if digit % 2 != 0: # Check if not even
                    Flag = False
                    break
            else:  # Odd index
                # Use the corrected prime digit check
                if not is_prime(digit):
                    Flag = False
                    break
        if Flag:
            count += 1
    return count
def recursion_method(n):
    if n==1:
        return 1
    num_str=str(n).zfill(len(str(n)))
    Flag=True
    for i in range(0,len(num_str),2):
        if int(num_str[i])%2==0:
            continue
        else:
            Flag=False
            break
    for i in range(1,len(num_str),2):
        if not is_prime(int(num_str[i])):
            Flag=False
            break
    if Flag:
        return recursion_method(n-1)+1
    else:
        return recursion_method(n-1)



print(count_good_numbers(4))
print(count_good_numbers_fixed_brute_force(4))
print(f"recursive method is", recursion_method((10**4)))


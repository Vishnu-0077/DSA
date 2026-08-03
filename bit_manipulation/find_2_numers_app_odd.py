def opt(arr):
    ans=0
    for val in arr:
        ans=ans^val
    xor_all = ans
    # find rightmost set bit
    set_bit = xor_all & -xor_all

    num1 = 0
    num2 = 0
    for val in arr:
        if val & set_bit: #if at the right most bit, value is 1, we are seperating num1 and num2 as we know that num1 and num2 has either 1 and other has 0, as the xor value is 1(they are not same)
            num1 ^= val
        else:
            num2 ^= val #understood. what happend? if xor is not zera, they have a setbit differing at some position

    return num1, num2
print(f"the numbers are {opt([1,1,3,4,4,5])}")

def swap_2_numbers(a,b):
    a=a^b
    b=a^b
    a=a^b
    return a,b
print(f"after swapping {(2,3)} the result is {swap_2_numbers(2,3)}")
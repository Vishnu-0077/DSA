#recursion code for printing numbers from 1 to n

def print_n_numbers(n):
    if n==0:
        return
    print_n_numbers(n-1)
    print(n)

print(print_n_numbers(5))
    
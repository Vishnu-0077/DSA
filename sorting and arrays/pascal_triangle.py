def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact


def pascal_triangle_row_and_clmn(n,r):
    if n>r:
        return factorial(n-1) // (factorial(r-1) * factorial(n - r))
    if n==r or n==0 or r==0:
        return 1

def pascal_triangle_row(n):
    row=[]
    for i in range(n):
        row.append(factorial(n-1) // (factorial(i) * factorial(n - i -1)))
    return row

#print(pascal_triangle_row_and_clmn(5, 3))  # Output: 10
print(pascal_triangle_row(10))  # Output: [1, 5, 10, 10, 5, 1]
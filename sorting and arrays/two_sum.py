def two_sum(array,result):
    n= len(array)
    for i in range(n):
        for j in range(i+1,n):
            if  array[i]+array[j]==result and i!=j:
                Flag=True
                return Flag, i, j
    Flag=False
    return Flag, -1,-1

result=int(input("Enter the target sum: "))
array = list(map(int,input().split()))
answer, i, j = two_sum(array, result)
if not answer:
    print("No such numbers found")
else:
    print(f"Numbers at index {i} and {j} add up to {result}: {array[i]} + {array[j]} = {result}")
# Example usage:
# array = [1, 2, 3, 4, 5]
# result = 6
# answer, i, j = two_sum(array, result)
# if not answer:     
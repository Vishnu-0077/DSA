def sol(arr):
    if arr==[]:
        return [[]]
    first = arr[0]
    rest_subset = sol(arr[1:])
    with_first = [[first]+subset for subset in rest_subset]
    return with_first+rest_subset

arr = [1,2,3]
print(sol(arr))
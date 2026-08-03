def brute_force_not_contigious(arr,sub_arrays):
    if arr not in sub_arrays and arr:
        sub_arrays.append(min(arr))
    for i in range(len(arr)):
        c_arr=arr.copy()
        c_arr.remove(arr[i])
        brute_force_not_contigious(c_arr,sub_arrays)
    return sub_arrays


def brute_force(arr):
    sub_arrays=[]
    for i in range(len(arr)):
        for j in range(i+1,len(arr)+1):
            sub_arrays.append(min(arr[i:j]))
    return sum(sub_arrays)


def optimized_using_stack(arr):
    stack=[]
    def find_the_next_smallest_number(arr,i,stack):
        if i==len(arr)-1:
            return len(arr)
        for j in range(len(arr)-1,i,-1):
            stack.append(j)
        while stack and arr[i]<=arr[stack[-1]]:
            stack.pop()
        ans=stack[-1] if stack else -1
        stack.clear()
        if ans!=-1:
            return ans
        else:
            return len(arr)
        
    def find_the_previous_smallest_number(arr,i,stack):
        if i==0:
            return -1
        for j in range(0,i):
            stack.append(j)
        while stack and arr[i]<=arr[stack[-1]]:
            stack.pop()
        ans=stack[-1] if stack else -1
        stack.clear()
        if ans!=-1:
            return ans
        else:
            return -1
    min_sum=0
    i=0
    while i<len(arr):
        min_value=arr[i]*(((i-find_the_previous_smallest_number(arr,i,stack))*(find_the_next_smallest_number(arr,i,stack)-i))-1)
        min_sum+=min_value
        i+=1
    return min_sum

    #instead of using 2 defin functions we can just use 2 lists to save, this will give O(n)
    def optimized_using_stack(arr):
        n = len(arr)
        next_smaller = [n] * n
        prev_smaller = [-1] * n
        stack = []

        # Compute previous smaller for each element
        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            prev_smaller[i] = stack[-1] if stack else -1
            stack.append(i)

        stack.clear()

        # Compute next smaller for each element
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] > arr[i]:  # strictly greater for next smaller
                stack.pop()
            next_smaller[i] = stack[-1] if stack else n
            stack.append(i)

        # Compute the sum of contributions
        min_sum = 0
        for i in range(n):
            left = i - prev_smaller[i]
            right = next_smaller[i] - i
            min_sum += arr[i] * left * right

        return min_sum




if __name__ == '__main__':
    arr = [11,81,94,43,3]
    print(brute_force_not_contigious(arr,[]))
    print()
    print("the brute force answer of the contigious arrays are:")
    print(brute_force(arr))
    print()
    print("after using the stack with next smaller and previous smaller")
    print(optimized_using_stack(arr))


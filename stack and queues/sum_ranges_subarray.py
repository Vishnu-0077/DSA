#for finding the next greater or next smaller and smaller greater, next prev, should be in finger tips

def stack_method(arr):
    stack=[]
    n=len(arr)
    next_greater=[n]*n
    prev_greater=[-1]*n
    next_smaller=[n]*n
    prev_smaller=[-1]*n
    for i in range(n-1,-1,-1):
        while stack and arr[stack[-1]]<arr[i]:
            stack.pop()
        next_greater[i]=stack[-1] if stack else n
        stack.append(i) 

    stack.clear()

    for i in range(n):
        while stack and arr[stack[-1]]<=arr[i]:
            stack.pop()
        prev_greater[i]=stack[-1] if stack else -1
        stack.append(i)
    stack.clear()
    
    for i in range(n-1,-1,-1):
        while stack and arr[stack[-1]]>arr[i]:
            stack.pop()
        next_smaller[i]=stack[-1] if stack else n
        stack.append(i)
    stack.clear()
    
    for i in range(n):
        while stack and arr[stack[-1]]>=arr[i]:
            stack.pop()
        prev_smaller[i]=stack[-1] if stack else -1
        stack.append(i)
    stack.clear()
    
    sum_min=0
    sum_max=0
    for i in range(n): #it should be sigma(subarray_max)-sigma(subarray_min)
        left_min = i - prev_smaller[i]
        right_min = next_smaller[i] - i
        sum_min+=arr[i]*left_min*right_min
        left_max = i - prev_greater[i]
        right_max = next_greater[i] - i
        sum_max+=arr[i]*left_max*right_max
    return sum_max-sum_min

if __name__ == "__main__":
    arr = [1,3,3]
    print(stack_method(arr))


    
            

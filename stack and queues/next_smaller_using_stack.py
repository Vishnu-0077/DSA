def monotonic_stack_solution(n,arr):
    stack = []
    ans = [-1]*n #this is not in circular
    for i in range(1,n+1):
        while stack and arr[-i]<=stack[-1]:
            stack.pop()
        if stack:
            ans[-i]=stack[-1]
        stack.append(arr[-i])
    return ans

if __name__ == '__main__':
    arr = [4, 8, 5, 2, 25]
    n=len(arr)
    print(monotonic_stack_solution(n,arr))
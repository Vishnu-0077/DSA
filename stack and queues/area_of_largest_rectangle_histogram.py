def own_stack(n,heights):
    stack=[]
    next_smallest=[n]*n
    prev_smallest=[-1]*n
    for i in range(n-1,-1,-1):
        while stack and heights[stack[-1]]>=heights[i]:
            stack.pop()
        next_smallest[i]=stack[-1] if stack else n
        stack.append(i)
    stack.clear()

    for i in range(n):
        while stack and heights[stack[-1]]>=heights[i]:
            stack.pop()
        prev_smallest[i]=stack[-1] if stack else -1
        stack.append(i)
    stack.clear()

    areas=[]
    for i in range(n):
        areas.append(heights[i]*(next_smallest[i]-prev_smallest[i]-1)) #next smallest varaikum... so we look only the big guys
    return max(areas)

heights = [2,1,5,6,2,3]
n=6
print(own_stack(n,heights))

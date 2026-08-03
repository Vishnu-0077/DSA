def own(asteroids):
    n=len(asteroids)
    stack=[]
    for i in range(n):
        while stack and stack[-1]*asteroids[i]<0:
            if abs(stack[-1])<abs(asteroids[i]):
                stack.pop()
                continue
            elif abs(stack[-1]==abs(asteroids[i])):
                stack.pop()
                break
            else:
                break
        else: #the -5 wont be appended bcoz the while statement is still true, it broke out only because on the break statement, so -5 wont be appended

            stack.append(asteroids[i])
    return stack

asteroids = [10,2,-5,20,-3]
print(own(asteroids))


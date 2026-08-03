def opt(num1,num2):
    ans=num1^num2
    binary=bin(ans)[2:]
    count=0
    for i in binary:
        if i=='1':
            count+=1
    
    return count

print(opt(4,14))


    
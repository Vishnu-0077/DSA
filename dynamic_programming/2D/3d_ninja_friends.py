def rec(matrix,m1,n1,m2,n2):
    if (n1<0 or n1>=len(matrix[0])) or (n2<0 or n2>=len(matrix[0])):
        return 0
    if m1==len(matrix)-1:
        if n1==n2:
            return matrix[m1][n1]
        else:
            return matrix[m1][n1]+matrix[m2][n2]
    
    maxi = -1
    
    for di in [-1,0,1]:
        for dj in [-1,0,1]:
            if n1+di<0 or n1+di>=len(matrix[0]) or n2+dj<0 or n2+dj>=len(matrix[0]):
                continue
            if m1==m2 and n1==n2:
                result = matrix[m1][n1] + rec(matrix,m1+1,n1+di,m2+1,n2+dj)
                maxi = max(result,maxi)
            else:
                result = matrix[m1][n1]+ matrix[m2][n2] + rec(matrix,m1+1,n1+di,m2+1,n2+dj)
                maxi = max(result,maxi)

    return maxi
#that was the recursion method.....     
    

Grid = [[2, 3, 1, 2], [3, 4, 2, 2], [5, 6, 3, 5]]
print(rec(Grid,0,0,0,len(Grid[0])-1))

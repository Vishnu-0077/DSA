#intuition.... start will all the possibl epositions and then dfs it.... store the visited
#constrain the boundaries... u don have to go to the edge of the matrix... as that is the question
#store the visited and then change it...

def dfs(matrix,visited,x,y):
    visited.add((x,y))
    directions = [[1,0],[-1,0],[0,1],[0,-1]]
    for way in directions:
        i,j = way[0],way[1]
        xn,yn = x+i,y+j
        if xn<0 or yn<0 or xn>=len(matrix) or yn>=len(matrix[0]):
            return None
        elif (0<=xn<len(matrix) and 0<=yn<len(matrix[0]) and (xn,yn) not in visited and matrix[xn][yn] == 'O'):
            return dfs(matrix,visited,xn,yn)
    return visited

def main(matrix):
    visited = set()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 'O':
                visited = dfs(matrix,set(),i,j)
                if visited:
                    for x,y in visited:
                        matrix[x][y] = 'X'
    return matrix

if __name__ == '__main__':
    matrix = [
        ['X','X','X','X'],
        ['X','O','X','X'],
        ['X','O','O','X'],
        ['X','O','X','X'],
        ['X','X','O','O']
    ]

    for x in matrix:
        print(x)

    print()
        
    ans = main(matrix)
    for x in ans:
        print(x)
        
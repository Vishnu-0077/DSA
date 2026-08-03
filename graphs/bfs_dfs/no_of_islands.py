def dfs(matrix,x,y,visited):
    if (x,y) is visited:
        return 
    visited.add((x,y))
    for i in range(-1,2):
        for j in range(-1,2):
            xn = x+i
            yn = y+j
            if 0<=xn<len(matrix) and 0<=yn<len(matrix[0]) and (xn,yn) not in visited and matrix[xn][yn] == '1':
                dfs(matrix,xn,yn,visited)

def main(matrix):
    visited = set()
    count = 0
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            if (x,y) not in visited:
                if matrix[x][y] == '1':
                    dfs(matrix,x,y,visited)
                    count += 1
    return count

if __name__ == "__main__":
    grid = [
        ['1','1','0','1','1'],
        ['1','1','0','0','0'],
        ['0','0','0','1','0'],
        ['0','0','0','1','1']
    ]

    for x in grid:
        print(x)

    print()

    print(main(grid))
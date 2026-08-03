def dfs(matrix,x,y,visited,effort):
    if {x,y} == {len(matrix)-1,len(matrix[0])-1}:
        return effort
    visited.add((x,y))
    mini = float('inf')
    directions = [[1,0],[-1,0],[0,1],[0,-1]]
    for way in directions:
        i,j = way[0],way[1]
        xn,yn = x+i, y+j
        if (0<=xn<len(matrix) and 0<=yn<len(matrix[0])) and (xn,yn) not in visited:
            result = dfs(matrix,xn,yn,visited,effort)
            result = result+abs(matrix[x][y]-matrix[xn][yn])
            mini = min(mini,result)
    visited.remove((x,y))
    return mini

def main(matrix):
    visited = set()
    return dfs(matrix,0,0,visited,0)

import heapq

def heap_method(matrix):
    heap = []
    effort_matrix = []
    for i in range(len(matrix)):
        effort_matrix.append([float('inf')]*len(matrix[0]))
    heapq.heappush(heap,[0,[0,0]])
    while heap:
        effort,node = heapq.heappop(heap)
        if effort>effort_matrix[node[0]][node[1]]:
            continue
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        for way in directions:
            i,j = way[0],way[1]
            xn,yn = node[0]+i,node[1]+j
            if (0<=xn<len(matrix) and 0<=yn<len(matrix[0])):
                new_effort = effort+abs(matrix[node[0]][node[1]]-matrix[xn][yn])
                if effort_matrix[xn][yn] > new_effort:
                    effort_matrix[xn][yn] = new_effort
                    heapq.heappush(heap,[new_effort,[xn,yn]])
    return effort_matrix[len(matrix)-1][len(matrix[0])-1]

    


if __name__ == '__main__':
    matrix = [[1, 2, 1, 1, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1]]
    for x in matrix:
        print(x)
    print(main(matrix))
    print(heap_method(matrix))
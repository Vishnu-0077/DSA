def dfs(matrix,x,y,visited,count):
    if {x,y} == stop:
        return count
    visited.add((x,y))
    mini = float('inf')
    directions = [[1,0],[-1,0],[0,1],[0,-1]]
    for way in directions:
        i,j = way[0],way[1]
        xn,yn = x+i, y+j
        if (0<=xn<len(matrix) and 0<=yn<len(matrix[0])) and (xn,yn) not in visited and matrix[xn][yn] == '1':
            result = dfs(matrix,xn,yn,visited,count+1)
            mini = min(mini,result)
    return mini 

def main(matrix,start,stop):
    visited = set()
    x,y = start
    return dfs(matrix,x,y,visited,0)

#cant use a heapmap here... the heapmap can be used only when. have to go randomly
#ila i will use heap...
import heapq

def heap_method(matrix,start,stop): #dijikstra keeps note of all the distances from the start node
    start = list(start)
    stop = list(stop)
    heap = []
    d_matrix = []
    for i in range(len(matrix)):
        d_matrix.append([float('inf')]*len(matrix[0]))
    d_matrix[start[0]][start[1]] = 0
    heapq.heappush(heap,[0,start])
    while heap:
        dist,node = heapq.heappop(heap)
        if dist>d_matrix[node[0]][node[1]]:
            continue
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        for way in directions:
            i,j = way[0],way[1]
            xn,yn = node[0]+i,node[1]+j
            new_dist = dist+1
            if (0<=xn<len(matrix) and 0<=yn<len(matrix[0])) and matrix[xn][yn] == '1' and d_matrix[xn][yn] > new_dist:
                d_matrix[xn][yn] = new_dist
                heapq.heappush(heap,[new_dist,[xn,yn]])
    if d_matrix[stop[0]][stop[1]] == float('inf'):
        return -1
    return d_matrix[stop[0]][stop[1]]



if __name__ == "__main__":
    grid = [
        ['1','1','0','1','1'],
        ['1','1','0','0','0'],
        ['0','1','1','1','0'],
        ['0','0','0','1','1']
    ]
    start = {0,1}
    stop = {2,3}

    for x in grid:
        print(x)
    print()
    print(main(grid,start,stop))
    print()
    print(heap_method(grid,start,stop))
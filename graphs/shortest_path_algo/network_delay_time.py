def organize(matrix,n):
    ans = []
    for i in range(n):
        ans.append([])
    for j in range(len(matrix)):
        ans[matrix[j][0]].append([matrix[j][1], matrix[j][2]])
    return ans

def dfs(matrix,node,visited,count):
    if node == stop:
        visited.add(node)
        return count
    visited.add(node)
    mini = float('inf')
    for neighbour in matrix[node]:
        if neighbour[0] not in visited:
            dis = neighbour[1]
            result = dfs(matrix,neighbour[0],visited,count+dis)
            mini = min(result,mini)
    return mini

def main(matrix,n,start,stop):
    visited = set()
    dis = 0
    counted = dfs(matrix,start,visited,0)
    return counted




if __name__ == "__main__":
    times = [[2,1,1],[2,3,1],[3,4,1]]
    n = 4
    start = times[0][0]
    stop = times[-1][1]
    matrix = organize(times,4)
    print(matrix)
    print(main(matrix,n,start,stop))
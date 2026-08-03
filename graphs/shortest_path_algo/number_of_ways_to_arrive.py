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
    visited.remove(node)
    return mini

def main(matrix,n,start,stop):
    visited = set()
    dis = 0
    counted = dfs(matrix,start,visited,0)
    return counted

def dfs_2(matrix,node,visited,count,ans):
    if node == stop:
        if count == min_time:
            ans+=1
        return ans
    visited.add(node)
    for neighbour in matrix[node]:
        if neighbour[0] not in visited:
            dis = neighbour[1]
            ans = dfs_2(matrix,neighbour[0],visited,count+dis,ans)       
    visited.remove(node)
    return ans

def main_2(matrix,n,start,stop,min_time):   
    visited = set()
    counted = dfs_2(matrix,start,visited,0,0)
    return counted



if __name__ == "__main__":
    times = [[0, 6, 7], [0, 1, 2], [1, 2, 3], [1, 3, 3], [6, 3, 3], [3, 5, 1], [6, 5, 1], [2, 5, 1], [0, 4, 5], [4, 6, 2]]
    n = 7
    start = 0
    stop = n-1
    matrix = organize(times,n)
    print(matrix)
    min_time = main(matrix,n,start,stop)
    print(min_time)
    print(main_2(matrix,n,start,stop,min_time))
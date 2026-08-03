def organize(matrix,n): #we organice the given input in our form into an undirectedx
    ans = []
    for i in range(n):
        ans.append([])
    for j in range(n*2):
        ans[matrix[j][0]].append(matrix[j][1])
    return ans

def dfs(matrix,node,visited,count):
    if node == 0:
        return count
    visited.add(node)
    mini = float('inf')
    for neighbour in matrix[node]:
        if neighbour not in visited:
            result = dfs(matrix,neighbour,visited,count+1)
            mini = min(mini,result)
    visited.remove(node) #here we are removing nodes, because we are in a cyclic graph. not removing will affect the other cyclic paths
    return mini


def main(matrix,n):
    ans = []
    for node in range(n):
        visited = set()
        counted = dfs(matrix,node,visited,0)
        ans.append(counted)
    return ans

if __name__ == '__main__':
    matrix = [[0,1],[0,3],[3,4],[4 ,5],[5,6],[1,2],[2,6],[6,7],[7,8],[6,8]]
    for x in range(len(matrix)):
        matrix.append([matrix[x][1],matrix[x][0]])
    n = 10
    print(organize(matrix,n))
    matrix = organize(matrix,n)
    print(main(matrix,n))
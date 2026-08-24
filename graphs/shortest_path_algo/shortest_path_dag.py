#this is also little same like the before, but we have to take the distance as doubly graph and 
#take node[1] and neighbour and node[2] as the distance b/w the neigbour and node

def organize(matrix,n):
    ans = []
    for i in range(n):
        ans.append([])
    for j in range(n):
        ans[matrix[j][0]].append([matrix[j][1],matrix[j][2]])
    return ans

def dfs(matrix,node,visited,count):
    if node == 1:
        return count
    visited.add(node)
    mini = float('inf')
    for neighbour in matrix[node]:
        if neighbour[0] not in visited:
            dist = neighbour[1]
            result = dfs(matrix,neighbour[0],visited,count+dist)
            mini = min(mini,result)
    visited.remove(node)
    return mini

def main(matrix,n):
    ans = []
    for node in range(n):
        visited = set()
        counted = dfs(matrix,node,visited,0)
        ans.append(counted)
    return ans

if __name__ == '__main__':
    matrix = [[0,4,2], [0,5,3], [5,4,1], [4,6,3], [4,2,1], [6,1,2], [2,3,3], [1,3,1]]
    n = 8
    matrix = organize(matrix,n)
    print(matrix) 
    print(main(matrix,n))
    
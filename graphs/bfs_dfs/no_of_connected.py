def create_matrix(v):
    matrix = []
    for i in range(v):
        matrix.append([])
    for i in range(v):
        for j in range(v):
            matrix[i].append(0)
    return matrix
def add_edge(matrix,u,v):
    matrix[u][v] = 1
    matrix[v][u] = 1

def count_1(arr):
    count =0
    for x in arr:
        if x ==1:
            count+=1
    return count
def main(matrix):
    loops = 0
    Flag = True
    for x in matrix:
        if count_1(x) == 1 and Flag == True:
            loops += 1
            Flag = False
        elif count_1(x) == 1:
            Flag = True
        elif count_1(x) == 0:
            loops +=1
        else:
            continue
    return loops


v=4
edges=[[0,1], [2,3]]
matrix = create_matrix(v)
for x in edges:
    add_edge(matrix,x[0],x[1])
for x in matrix:
    print(x)
print(main(matrix))
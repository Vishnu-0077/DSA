#completely wrong topo_sort

def dfs(matrix,node,stack,final_stack,visited):
    if matrix[node] == []:
        final_stack.append(stack)
    visited.add(node)
    for neighbour in matrix[node]:
        stack_copy = stack.copy()
        stack_copy.append(neighbour)
        dfs(matrix,neighbour,stack_copy,final_stack,visited)

def getting_final_stack(matrix,n):
    final_stack = []
    visited = set()
    for node in range(n):
        if node not in visited:
            stack = []
            stack.append(node)
            dfs(matrix,node,stack,final_stack,visited)
            print(visited)
    return final_stack

def main(final_stack):
    ans = []
    for stack in final_stack:
        for node in stack[::-1]:
            if node not in ans:
                ans.insert(0,node)
    return ans


if __name__ == '__main__':
    n = 6
    adj = [[], [], [3], [1], [0, 1], [0, 2]]
    final_stack = getting_final_stack(adj,n)
    ans = main(final_stack)
    print(final_stack)
    print()
    print(ans)

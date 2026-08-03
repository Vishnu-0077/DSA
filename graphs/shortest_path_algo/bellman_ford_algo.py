def bellman_ford(adj,n):
    ans = []
    for i in range(n):
        ans.append(float('inf'))
    ans[0] = 0
    
    for i in range(n-1):
        for lst in adj:
            if ans[lst[0]]!=float('inf'):
                old_ans = ans[lst[1]]
                new_ans = ans[lst[0]]+lst[2]
                if new_ans<old_ans:
                    ans[lst[1]] = new_ans
    return ans

adj = [[3, 2, 6], [5, 3, 1], [0, 1, 5], [1, 5, -3], [1, 2, -2], [3, 4, -2], [2, 4, 3]]
n = 6
print(bellman_ford(adj,n))
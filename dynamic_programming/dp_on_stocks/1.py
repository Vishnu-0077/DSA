def space_opt(arr):
    mini = arr[0]
    profit = 0
    for i in range(1,len(arr)):
        cost = arr[i] - mini
        profit = max(profit,cost)
        mini = min(mini,arr[i])
    return profit   

print(space_opt([7,6,4,3,1]))

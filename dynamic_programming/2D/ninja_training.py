import time

def for_not_pick(lst,day,last): #for finding the 2nd largest and it's index
    maxi = float('-inf')
    max_previous = float('-inf')
    max_i = -1
    for i in range(len(lst)):
        if lst[i]>=maxi and i!=last:
            max_previous = maxi
            max_prev_i = max_i
            maxi = lst[i]
            max_i = i
        elif lst[i]>max_previous and lst[i]<maxi and i!=last:
            max_previous = lst[i]
            max_prev_i = i
    return max_previous,max_prev_i

def for_pick(lst,day,last): #for finding the largest and it's index
    maxi = float('-inf')
    for i in range(len(lst)):
        if lst[i]>=maxi and i!=last:
            maxi = lst[i]
            max_i = i
    return maxi,max_i


def own(matrix,day,last):
    if day<0:
        return 0

    pick_add_value, pick_index = for_pick(matrix[day],day,last)
    pick = pick_add_value + own(matrix,day-1,pick_index) #pick method if we picked the largest
    
    not_pick_add_value, not_pick_index = for_not_pick(matrix[day],day,last)
    not_pick = not_pick_add_value + own(matrix,day-1,not_pick_index) # not pick method if we picked the 2nd largest
    return max(pick,not_pick)

def dp_memo(matrix,day,last,dp):
    if day<0:
        return 0
    if dp[day][last]!=-1: #correct dhan dp will be in 2d array. bcoz for everyday, the ans changes based on the last, so for in a day for each last each value
        return dp[day][last]
    pick_add_value, pick_index = for_pick(matrix[day],day,last)
    pick = pick_add_value + dp_memo(matrix,day-1,pick_index,dp) #pick method if we picked the largest
    
    not_pick_add_value, not_pick_index = for_not_pick(matrix[day],day,last)
    not_pick = not_pick_add_value + dp_memo(matrix,day-1,not_pick_index,dp) # not pick method if we picked the 2nd largest
    dp[day][last] = max(pick,not_pick)
    return dp[day][last]


matrix = [[70, 40, 10], [180, 20, 5], [200, 60, 30]]
day = len(matrix)-1
last = -1
start1 = time.time()
print(own(matrix,day,last))
print(time.time()-start1)

start2 = time.time()
dp = [[-1]*len(matrix[0]) for _ in range(len(matrix))]
print(dp_memo(matrix,day,last,dp))
print(time.time()-start2)
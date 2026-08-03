import heapq

def priority_queue(arr,start,end):
    heap = []
    heapq.heappush(heap,[0,start])
    while heap:
        step,node = heapq.heappop(heap)
        if node > end:
            continue
        if node == end:
            return step
        for neigh in arr:
            new_node = (node*neigh)%10000
            new_step = step+1
            heapq.heappush(heap,[new_step,new_node])
    return -1

def dfs_method(arr,start,end):

    def dfs(arr,node,end,step):
        mini = float('inf')
        if node>end:
            return float('inf')
        if node == end:
            return step
        
        for neigh in arr:
            new_node = (node*neigh)%100000
            new_step = step+1
            result = dfs(arr,new_node,end,new_step)
            mini = min(result,mini)
        return mini

    
    def main(arr,start,end):
        step = 0
        count = dfs(arr,start,end,step)
        return count

    return main(arr,start,end)


if __name__ == '__main__':
    arr = [2,5,7]
    start = 3
    end = 30
    print(priority_queue(arr,start,end))
    print(dfs_method(arr,start,end))
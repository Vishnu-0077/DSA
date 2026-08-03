import heapq

def priority_queue(adj,n):
    ans = []
    for k in range(n):
        ans.append(float('inf'))
    ans[0] = 0
    heap = []
    heapq.heappush(heap,[0,0]) #do heapq.heapify(heap) to canvert a list to a heap
    while heap:
        dist,node = heapq.heappop(heap)
        if dist>ans[node]:
            continue
        for neighbour in adj[node]:
            new_dist = dist + neighbour[1]
            if new_dist<ans[neighbour[0]]:
                ans[neighbour[0]] = new_dist
                heapq.heappush(heap,[new_dist,neighbour[0]])
    return ans


if __name__ == "__main__":
    n = 6
    adj = [[] for _ in range(n)]
    adj[0].append((1,4))
    adj[0].append((2,4))
    adj[1].append((2,2))
    adj[1].append((0,4))
    adj[2].append((1,2))
    adj[2].append((0,4))
    adj[2].append((3,3))
    adj[2].append((4,1))
    adj[2].append((5,6))
    adj[3].append((2,3))
    adj[4].append((2,1))
    adj[3].append((5,2))
    adj[5].append((3,2))
    adj[5].append((2,6))
    adj[4].append((5,1))
    adj[5].append((4,1))

    print(priority_queue(adj,n))
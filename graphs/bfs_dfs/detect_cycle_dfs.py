#use dfs as usual and a parent node to track the previous node. then do dfs. main is same...majha dhan
#same process like the detect cycle in bfs but we are using dfs here

class Solution:
    # DFS function to detect cycle
    def dfs(self, node, parent, adj, visited):
        # Mark current node visited
        visited[node] = True

        # Traverse neighbors
        for neighbor in adj[node]:

            # If neighbor not visited, recurse
            if not visited[neighbor]:
                if self.dfs(neighbor, node, adj, visited):
                    return True

            # If neighbor visited and not parent, cycle exists
            elif neighbor != parent: #to prevent going in reverse
                return True

        # No cycle found from this path
        return False

    # Function to check cycle in graph
    def isCycle(self, V, adj):
        visited = [False] * V

        # Check all components
        for i in range(V):
            if not visited[i]:
                if self.dfs(i, -1, adj, visited):
                    return True
        return False


def main():
    # Example: Graph with 5 nodes and a cycle
    V = 5
    adj = [[] for _ in range(V)]

    # Add edges
    adj[0].append(1)
    adj[1].append(0)
    adj[1].append(2)
    adj[2].append(1)
    adj[2].append(3)
    adj[3].append(2)
    adj[3].append(4)
    adj[4].append(3)
    adj[4].append(1)  

    sol = Solution()
    if sol.isCycle(V, adj):
        print("Cycle detected")
    else:
        print("No cycle found")


if __name__ == "__main__":
    main()
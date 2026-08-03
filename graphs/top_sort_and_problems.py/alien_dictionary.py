def create_the_topology(graph,letter_list):
    topology = {}
    for i in range(len(graph)-1):
        lst = []
        for x in range(min(len(graph[i]),len(graph[i+1]))):
            if graph[i][x] != graph[i+1][x]:
                if graph[i][x] in topology:
                    topology[graph[i][x]].append(graph[i+1][x])
                else:
                    topology[graph[i][x]] = [graph[i+1][x]]
                break
            else:
                continue
    for x in letter_list:
        if x not in topology.keys():
            topology[x] = []
    return topology

def make_letter_list(graph):
    letter_list = []
    for word in graph:
        for letter in word:
            if letter not in letter_list:
                letter_list.append(letter)
    return ''.join(letter_list)

def dfs(topology,node,visited,stack):
    visited.add(node)
    for neighbour in topology[node]:
        if neighbour not in visited:
            dfs(topology,neighbour,visited,stack)
    stack.append(node)

def main(topology):
    visited = set()
    stack = []
    for node in topology.keys():
        if node not in visited:
            dfs(topology,node,visited,stack)
    return stack[::-1]




if __name__ == '__main__':
    graph = ["baa","abcd","abca","cab","cad"]
    letter_list = make_letter_list(graph)
    topology = create_the_topology(graph,letter_list)
    print(topology)
    print()
    print(main(topology))

                    


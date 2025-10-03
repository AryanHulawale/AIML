def dfs(graph, start, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []

    visited.add(start)
    path.append(start)

    for neighbour in graph.get(start, []):
        if neighbour not in visited:
            dfs(graph, neighbour, visited, path)

    return path

graph = {}
n = int(input("Enter number of nodes in the graph: "))

for _ in range(n):
    node = input("Enter node name: ")
    neighbours = input(f"Enter neighbors of {node} separated by space: ").split()
    graph[node] = neighbours

start_node = input("Enter the start node for DFS: ")

result = dfs(graph, start_node)
print("DFS Traversal Path:", result)

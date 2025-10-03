from queue import PriorityQueue

def greedy_bfs(graph, start, goal, heuristics):
    path = []
    pq = PriorityQueue()
    pq.put((heuristics[start], start))
    visited = set()

    while not pq.empty():
        priority, current = pq.get()

        if current in visited:
            continue

        path.append(current)
        visited.add(current)

        if current == goal:
            return path

        for neighbour in graph.get(current, []):
            if neighbour not in visited:
                pq.put((heuristics[neighbour], neighbour))

    return path

graph = {}
n = int(input("Enter number of nodes in the graph: "))

for _ in range(n):
    node = input("Enter node name: ")
    neighbours = input(f"Enter neighbors of {node} separated by space: ").split()
    graph[node] = neighbours

heuristics = {}
for node in graph:
    heuristics[node] = int(input(f"Enter heuristic value for {node}: "))

startNode = input("Enter start node: ")
goalNode = input("Enter goal node: ")

result = greedy_bfs(graph, startNode, goalNode, heuristics)
print("Greedy BFS : ", result)

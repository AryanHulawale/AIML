from queue import PriorityQueue


def a_star_easy(graph, start, goal, heuristics):
    visited = set()
    pq = PriorityQueue()
    pq.put((heuristics[start], start))
    path = []
    came_from = {}

    while not pq.empty():
        _, current = pq.get()

        if current in visited:
            continue

        visited.add(current)
        path.append(current)

        if current == goal:
            final_path = [current]
            while current in came_from:
                current = came_from[current]
                final_path.append(current)
            final_path.reverse()
            return final_path

        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                f_score = len(path) +  heuristics[neighbor]
                came_from[neighbor] = current
                pq.put((f_score, neighbor))

    return None


graph = {}
n = int(input("Enter number of nodes in the graph: "))

for _ in range(n):
    node = input("Enter node name: ")
    neighbours = input(f"Enter neighbors of {node} separated by space: ").split()
    graph[node] = neighbours

heuristics = {}
for node in graph:
    heuristics[node] = int(input(f"Enter heuristic value for {node}: "))

start_node = input("Enter start node: ")
goal_node = input("Enter goal node: ")


result = a_star_easy(graph, start_node, goal_node, heuristics)
print("A* Search Path:", result)


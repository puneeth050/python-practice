import heapq

def astar(graph, start, goal):
    open_set = []  # Priority queue to store nodes to be evaluated
    heapq.heappush(open_set, (0, start))  # Initialize the open set with the starting node
    came_from = {}  # To store the parent nodes for path reconstruction
    g_score = {node: float('inf') for node in graph}  # Cost from start to each node
    g_score[start] = 0
    f_score = {node: float('inf') for node in graph}  # Estimated total cost from start to goal
    f_score[start] = heuristic(start, goal)

    while open_set:
        current_f, current = heapq.heappop(open_set)

        if current == goal:
            return reconstruct_path(came_from, current)

        for neighbor in graph[current]:
            tentative_g_score = g_score[current] + graph[current][neighbor]

            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return None  # No path found

def heuristic(node, goal):
    # Define the heuristic function (Manhattan distance)
    x1, y1 = node
    x2, y2 = goal
    return abs(x1 - x2) + abs(y1 - y2)

def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    return list(reversed(path))

# Example usage:
graph = {
    (0, 0): {(0, 1): 5, (1, 0): 10},
    (0, 1): {(0, 0): 5, (1, 1): 10},
    (1, 0): {(0, 0): 10, (1, 1): 5, (2, 0): 20},
    (1, 1): {(0, 1): 10, (1, 0): 5, (2, 1): 5},
    (2, 0): {(1, 0): 20, (2, 1): 2},
    (2, 1): {(1, 1): 5, (2, 0): 2}
}

start_node = (0, 0)
goal_node = (2, 1)
path = astar(graph, start_node, goal_node)
print(path)  # The shortest path from (0, 0) to (2, 1)

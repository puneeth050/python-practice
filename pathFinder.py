import heapq
import matplotlib.pyplot as plt
import numpy as np

# Define grid dimensions
width = 7
height = 7

# Define the grid
grid = np.zeros((width, height))

# Define start and goal positions
start = (0, 0)
goal = (6, 6)

# Define obstacles
obstacles = [(0, 6), (4, 5)]

for obs in obstacles:
    grid[obs] = 1  # Mark obstacles with 1

# A* algorithm
def astar(grid, start, goal):
    # Implementation of the A* algorithm
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {pos: float('inf') for pos in np.ndindex(grid.shape)}
    g_score[start] = 0
    f_score = {pos: float('inf') for pos in np.ndindex(grid.shape)}
    f_score[start] = heuristic(start, goal)

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            return reconstruct_path(came_from, current)

        for neighbor in get_neighbors(current):
            tentative_g_score = g_score[current] + 1  # Assuming a cost of 1 to move between adjacent cells

            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return None

def heuristic(pos, goal):
    # Define the heuristic function (e.g., Manhattan distance)
    return abs(pos[0] - goal[0]) + abs(pos[1] - goal[1])

def get_neighbors(pos):
    # Get neighboring positions
    x, y = pos
    neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    return [n for n in neighbors if 0 <= n[0] < width and 0 <= n[1] < height and grid[n] != 1]

def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    return list(reversed(path))

# Visualize the grid
def visualize_grid(grid, path=[]):
    plt.imshow(grid, cmap='Blues')
    plt.colorbar()
    for (x, y) in path:
        plt.text(y, x, 'X', color='red', ha='center', va='center')
    plt.text(start[1], start[0], 'S', color='green', ha='center', va='center')
    plt.text(goal[1], goal[0], 'G', color='blue', ha='center', va='center')
    plt.xticks(range(width))
    plt.yticks(range(height))
    plt.gca().invert_yaxis()
    plt.grid()
    plt.show()

path = astar(grid, start, goal)
visualize_grid(grid, path)

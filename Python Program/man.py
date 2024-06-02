import tkinter as tk
from queue import PriorityQueue

def find_path(maze):
    num_rows = len(maze)
    num_cols = len(maze[0])
    movements = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = PriorityQueue()
    start_position = (0, 0)
    queue.put((0, start_position))  # Use priority queue with the priority as the heuristic value
    visited = set([start_position])
    parents = {}
    while not queue.empty():
        _, current_position = queue.get()
        if current_position == (num_rows - 1, num_cols - 1):
            break
        for movement in movements:
            next_row = current_position[0] + movement[0]
            next_col = current_position[1] + movement[1]
            if 0 <= next_row < num_rows and 0 <= next_col < num_cols and maze[next_row][next_col] == 0:
                next_position = (next_row, next_col)
                if next_position not in visited:
                    queue.put((heuristic(next_position, num_rows, num_cols), next_position))
                    visited.add(next_position)
                    parents[next_position] = current_position
    if queue.empty() and current_position != (num_rows - 1, num_cols - 1):
        return None
    path = []
    while current_position is not None:
        path.append(current_position)
        current_position = parents.get(current_position)
    path.reverse()
    return path

def heuristic(position, num_rows, num_cols):
    # Heuristic function - Manhattan distance to the goal
    goal_position = (num_rows - 1, num_cols - 1)
    return abs(position[0] - goal_position[0]) + abs(position[1] - goal_position[1])

def display_maze_with_path_gui(maze, path):
    root = tk.Tk()
    root.title("Maze Path")
    # Set the dimensions of the canvas based on the maze size
    cell_size = 80
    canvas_width = len(maze[0]) * cell_size
    canvas_height = len(maze) * cell_size
    canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
    canvas.pack(fill=tk.BOTH, expand=True)

    def draw_path(index):
        if index >= len(path):
            # Print the final path traversal after the node-by-node traversal
            print("Final Path Traversal:")
            for i, node in enumerate(path):
                print("Step {}: {}".format(i + 1, node))
            return
        current_position = path[index]
        for i in range(len(maze)):
            for j in range(len(maze[0])):
                x1 = j * cell_size
                y1 = i * cell_size
                x2 = x1 + cell_size
                y2 = y1 + cell_size
                if (i, j) == current_position:
                    canvas.create_rectangle(x1, y1, x2, y2, fill="yellow")  # current node
                elif maze[i][j] == 1:
                    canvas.create_rectangle(x1, y1, x2, y2, fill="black")  # walls
                else:
                    canvas.create_rectangle(x1, y1, x2, y2, fill="white")  # spaces

        root.after(500, draw_path, index + 1)

    draw_path(0)
    root.mainloop()

maze = [
    [0, 1, 0, 0, 0, 0, 1, 1, 1, 0],
    [0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 1, 1, 1, 0],
    [0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]
# Find the main path
main_path = find_path(maze)
if main_path is None:
    print("No path found.")
else:
    print("Path found!")
    # Display the maze with the main path and alternate paths
    display_maze_with_path_gui(maze, main_path)

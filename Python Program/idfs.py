def iddfs(graph, start_node, target_node, max_depth):
    for depth in range(max_depth + 1):
        visited = set()  # Set to track visited nodes
        stack = [(start_node, [start_node], 0)]  # Stack to simulate recursion with depth

        while stack:
            current_node, path, current_depth = stack.pop()

            if current_node == target_node:
                print("Traversed path:", " -> ".join(path))  # Print the traversed path
                return path  # Return the path if the target node is found

            if current_depth <= depth:  # Updated condition
                if current_node not in visited:
                    visited.add(current_node)
                    neighbors = graph[current_node]

                    # Push unvisited neighbors onto the stack along with the path and increased depth
                    for neighbor in neighbors[::-1]:
                        if neighbor not in visited:
                            stack.append((neighbor, path + [neighbor], current_depth + 1))

    return []  # Empty list if no path is found


romania_graph = {
    'Arad': ['Zerind', 'Timisoara', 'Sibiu'],
    'Zerind': ['Oradea', 'Arad'],
    'Timisoara': ['Lugoj', 'Arad'],
    'Sibiu': ['Fagaras', 'Rimnicu Vilcea', 'Arad', 'Oradea'],
    'Oradea': ['Zerind', 'Sibiu'],
    'Lugoj': ['Mehadia', 'Timisoara'],
    'Fagaras': ['Bucharest', 'Sibiu'],
    'Rimnicu Vilcea': ['Craiova', 'Pitesti', 'Sibiu'],
    'Mehadia': ['Drobeta', 'Lugoj'],
    'Drobeta': ['Craiova', 'Mehadia'],
    'Craiova': ['Drobeta', 'Rimnicu Vilcea', 'Pitesti'],
    'Pitesti': ['Bucharest', 'Craiova', 'Rimnicu Vilcea'],
    'Bucharest': ['Urziceni', 'Pitesti', 'Fagaras'],
    'Giurgiu': ['Bucharest'],
    'Urziceni': ['Hirsova', 'Vaslui', 'Bucharest'],
    'Hirsova': ['Eforie', 'Urziceni'],
    'Vaslui': ['Iasi', 'Urziceni'],
    'Iasi': ['Neamt', 'Vaslui'],
    'Neamt': ['Iasi'],
    'Eforie': ['Hirsova']
}

source_node = input("Enter the source node: ")
destination_node = input("Enter the destination node: ")
max_depth = int(input("Enter the maximum depth: "))

for depth in range(max_depth + 1):
    print(f"Paths at depth {depth}:")
    path = iddfs(romania_graph, source_node, destination_node, depth)
    
    if path:
        print(" -> ".join(path))
    else:
        print("No path exists.")

    print()  # Print a new line after each iteration

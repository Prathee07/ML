def best_first_search(graph, start, goal, heuristic):
    # Initialize the open list with the start node
    open_list = [(heuristic[start], start, 0, [])]
    closed_list = set()
    
    while open_list:
        # Sort the open list based on heuristic value
        open_list.sort(key=lambda x: x[0], reverse=True)
        # Pop the node with the lowest heuristic value
        h_value, node, cost, path = open_list.pop()
        # Update the path
        path = path + [node]

        # If the goal is reached, return the cost and path
        if node == goal:
            return cost, path

        # Add the current node to the closed list
        closed_list.add(node)

        # Expand the node's neighbors
        for neighbour, neighbour_cost in graph[node]:
            if neighbour not in closed_list:
                # Calculate the new cost
                new_cost = cost + neighbour_cost
                # Add the neighbor to the open list
                open_list.append((heuristic[neighbour], neighbour, new_cost, path))

    return None

# Define the graph
graph = {
    'A': [('B', 11), ('C', 14), ('D', 7)],
    'B': [('A', 11), ('E', 15)],
    'C': [('A', 14), ('E', 8), ('D', 18), ('F', 10)],
    'D': [('A', 7), ('F', 25), ('C', 18)],
    'E': [('B', 15), ('C', 8), ('H', 9)],
    'F': [('G', 20), ('C', 10), ('D', 25)],
    'G': [],
    'H': [('E', 9), ('G', 10)]
}

# Define the heuristic values
heuristic = {
    'A': 40,
    'B': 32,
    'C': 25,
    'D': 35,
    'E': 19,
    'F': 17,
    'G': 0,
    'H': 10
}

# Perform the search
start = 'A'
goal = 'G'
result = best_first_search(graph, start, goal, heuristic)

# Print the result
if result:
    print(f"Minimum cost path from {start} to {goal} is {result[1]}")
    print(f"Cost: {result[0]}")
else:
    print(f"No path from {start} to {goal}")

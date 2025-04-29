from collections import deque
# def bfs , set of visited, queue first element as start
#while queue pop and add in vertex, if it is not visited then add it after printing
#now neighbor is not in visited add it in queue
def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            print(vertex, end=" ")
            visited.add(vertex)

            for neighbor in graph.get(vertex, []):#ratta
                if neighbor not in visited:
                    queue.append(neighbor)

# --- Taking input from the user ---
graph = {}

num_nodes = int(input("Enter number of nodes: "))

for _ in range(num_nodes):
    node = input("Enter node name: ")
    neighbors = input(f"Enter neighbours of {node} separated by space: ").split()
    graph[node] = neighbors

start_node = input("Enter the starting node for BFS traversal: ")

print("\nBFS Traversal is:")
bfs(graph, start_node)

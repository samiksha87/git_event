N =8
board = [[0 for i in range(N)] for i in range(N)]

def check_column(board, row, column):
    for i in range(row):
        #column is fixed 
        if board[i][column] == 1:
            return False
    return True

#check for top left and top right 
def check_diagonal(board, row, column):
    #top left
    for i,j in zip(range(row, -1, -1), range(column, -1,-1)):
        if board[i][j] == 1:
            return False
    
    #top right
    for i,j in zip(range(row, -1, -1), range(column, N)):
        if board[i][j] == 1:
            return False
    return True

def NQueen(board, row):
    if row == N:
        return True
    for i in range(N):
        if(check_column(board, row, i)==True and check_diagonal(board, row, i)==True):
            board[row][i] = 1
            if(NQueen(board, row+1)):
                return True
            board[row][i] = 0
    return False
NQueen(board, 0)
for row in board:
    print(row)
    
    
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    print(start, end=" ")
    visited.add(start)

    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# --- Taking input from the user ---
graph = {}

num_nodes = int(input("Enter number of nodes: "))

for _ in range(num_nodes):
    node = input("Enter node name: ")
    neighbors = input(f"Enter neighbours of {node} separated by space: ").split()
    graph[node] = neighbors

start_node = input("Enter the starting node for DFS traversal: ")

print("\nDFS Traversal is:")
dfs(graph, start_node)

# Initialize an empty 9x9 board with zeros
board = [[0 for _ in range(9)] for _ in range(9)]

# Populate the board with some values (example logic)
for i in range(len(board)):
    for j in range(len(board[0])):
        board[i][j] = (i + j) % 9 + 1  # Example: Assign numbers 1-9 in a pattern

# Print the board
for row in board:
    print(row)


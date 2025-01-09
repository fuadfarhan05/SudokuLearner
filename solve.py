board = [
    [7, 8, " ", 4, " ", " ", 1, 2, " "],
    [6, " ", " ", " ", 7, 5, " ", " ", 9],
    [" ", " ", " ", 6, " ", 1, " ", 7, 8],
    [" ", " ", 7, " ", 4, " ", 2, 6, " "],
    [" ", " ", 1, " ", 5, " ", 9, 3, " "],
    [9, " ", 4, " ", 6, " ", " ", " ", 5],
    [" ", 7, " ", 3, " ", " ", " ", 1, 2],
    [1, 2, " ", " ", " ", 7, 4, " ", " "],
    [" ", 4, 9, 2, " ", 6, " ", " ", 7]
]

''' [try more boards below ]
[5, 3, " ", " ", 7, " ", " ", " ", " "],
    [6, " ", " ", 1, 9, 5, " ", " ", " "],
    [" ", 9, 8, " ", " ", " ", " ", 6, " "],
    [8, " ", " ", " ", 6, " ", " ", " ", 3],
    [4, " ", " ", 8, " ", 3, " ", " ", 1],
    [7, " ", " ", " ", 2, " ", " ", " ", 6],
    [" ", 6, " ", " ", " ", " ", 2, 8, " "],
    [" ", " ", " ", 4, 1, 9, " ", " ", 5],
    [" ", " ", " ", " ", 8, " ", " ", 7, 9]

     [8, " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", 3, 6, " ", " ", " ", " ", " "],
    [" ", 7, " ", " ", 9, " ", 2, " ", " "],
    [" ", 5, " ", " ", " ", 7, " ", " ", " "],
    [" ", " ", " ", " ", 4, 5, 7, " ", " "],
    [" ", " ", " ", 1, " ", " ", " ", 3, " "],
    [" ", " ", 1, " ", " ", " ", " ", 6, 8],
    [" ", " ", 8, 5, " ", " ", " ", 1, " "],
    [" ", 9, " ", " ", " ", " ", 4, " ", " "]



    '''


def valid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False

    return True


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("----------------------")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == " ":
                return (i, j)  # row, col

    return None

def valid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False

    return True

def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = " "

    return False






print("_______Sudoku Board_______")
print_board(board)
solve(board)

print("                          ")
print("                          ")
print("                          ")
print("                          ")

print("________ Solved! _________")
print_board(board)

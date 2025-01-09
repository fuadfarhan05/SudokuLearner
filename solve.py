import random

def generate_New():
    board = [[0 for _ in range(9)] for _ in range(9)]

    def fill_board(bo):
        for i in range(9):
            for j in range(9):
                if bo[i][j] == 0:
                    numbers = list(range(1, 10))
                    random.shuffle(numbers)
                    for num in numbers:
                        if valid(bo, num, (i, j)):
                            bo[i][j] = num
                            if fill_board(bo):
                                return True
                            bo[i][j] = 0
                    return False
        return True
    fill_board(board)

    for _ in range(random.randint(40, 50)):  # Adjust for difficulty
        row, col = random.randint(0, 8), random.randint(0, 8)
        board[row][col] = " "

    return board


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
    print()


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


# Main program
print("Generating a New Sudoku Board:")
board = generate_New()
print_board(board)

print("Solving the Sudoku Board:")
solve(board)
print_board(board)

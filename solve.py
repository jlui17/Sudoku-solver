puzzle = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
]


def check_horizontal(y, v):
    for x in range(9):
        if v == puzzle[y][x]:
            return False
    return True


def check_vertical(x, v):
    for y in range(9):
        if v == puzzle[y][x]:
            return False
    return True


def check_square(top_left_x, top_left_y, v):
    for offset_y in range(3):
        for offset_x in range(3):
            if v == puzzle[top_left_y + offset_y][top_left_x + offset_x]:
                return False
    return True


def print_puzzle(grid):
    output = ""
    for i in range(9):
        for j in range(9):
            output += (str(grid[i][j]) + " ")
        output += "\n"
    print(output)


print_puzzle(puzzle)

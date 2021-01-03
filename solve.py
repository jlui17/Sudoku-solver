puzzle = [
    [0, 0, 0, 7, 0, 4, 0, 0, 0],
    [7, 0, 1, 0, 0, 0, 3, 0, 0],
    [0, 0, 5, 0, 0, 0, 0, 0, 9],
    [0, 0, 0, 0, 0, 0, 0, 5, 0],
    [9, 3, 0, 6, 0, 0, 0, 0, 8],
    [0, 0, 0, 8, 0, 0, 0, 0, 1],
    [1, 4, 0, 2, 0, 0, 8, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 4],
    [0, 0, 0, 0, 9, 0, 7, 6, 0],
]


# checks if v is not in the specified row
def check_horizontal(y, v):
    for x in range(9):
        if v == puzzle[y][x]:
            return False
    return True


# checks if v is not in the specified column
def check_vertical(x, v):
    for y in range(9):
        if v == puzzle[y][x]:
            return False
    return True


# checks if v is not in the specified square
def check_square(top_left_x, top_left_y, v):
    for offset_y in range(3):
        for offset_x in range(3):
            if v == puzzle[top_left_y + offset_y][top_left_x + offset_x]:
                return False
    return True


# checks if we can put v into that spot in the puzzle
def check_valid(x, y, v):
    top_left_x, top_left_y = x//3*3, y//3*3
    return check_horizontal(y, v) and check_vertical(x, v) and check_square(top_left_x, top_left_y, v)


# find empty spot
def find_empty():
    for y in range(9):
        for x in range(9):
            if puzzle[y][x] == 0:
                return y, x


# solve the puzzle
def solve():
    empty = find_empty()
    # base case
    if not empty:
        return True
    else:
        y, x = empty

    for v in range(1, 10):
        if check_valid(x, y, v):
            puzzle[y][x] = v

            if solve():
                return True

            puzzle[y][x] = 0

    return False


# print puzzle
def print_puzzle(grid):
    output = ""
    for i in range(9):
        for j in range(9):
            output += (str(grid[i][j]) + " ")
        output += "\n"
    print(output)


print_puzzle(puzzle)
print("\n------------------------------")
solve()
print_puzzle(puzzle)

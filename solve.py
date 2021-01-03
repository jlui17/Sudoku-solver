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
def check_horizontal(y, v, grid):
    for x in range(9):
        if v == grid[y][x]:
            return False
    return True


# checks if v is not in the specified column
def check_vertical(x, v, grid):
    for y in range(9):
        if v == grid[y][x]:
            return False
    return True


# checks if v is not in the specified square
def check_square(top_left_x, top_left_y, v, grid):
    for offset_y in range(3):
        for offset_x in range(3):
            if v == grid[top_left_y + offset_y][top_left_x + offset_x]:
                return False
    return True


# checks if we can put v into that spot in the puzzle
def check_valid(x, y, v, grid):
    top_left_x, top_left_y = x//3*3, y//3*3
    return check_horizontal(y, v, grid) and check_vertical(x, v, grid) and check_square(top_left_x, top_left_y, v, grid)


# find empty spot
def find_empty(grid):
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                return y, x


# solve the puzzle
def solve(grid):
    empty = find_empty(grid)
    # base case
    if not empty:
        return True
    else:
        y, x = empty

    for v in range(1, 10):
        if check_valid(x, y, v, grid):
            grid[y][x] = v

            if solve(grid):
                return True

            grid[y][x] = 0

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
solve(puzzle)
print_puzzle(puzzle)

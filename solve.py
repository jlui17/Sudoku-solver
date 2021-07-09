class Solver:

    def __init__(self, puzzle):
        self.puzzle = puzzle


    # checks if v is not in the specified row
    def check_horizontal(self, y, v, grid):
        for x in range(9):
            if v == grid[y][x]:
                return False
        return True


    # checks if v is not in the specified column
    def check_vertical(self, x, v, grid):
        for y in range(9):
            if v == grid[y][x]:
                return False
        return True


    # checks if v is not in the specified square
    def check_square(self, top_left_x, top_left_y, v, grid):
        for offset_y in range(3):
            for offset_x in range(3):
                if v == grid[top_left_y + offset_y][top_left_x + offset_x]:
                    return False
        return True


    # checks if we can put v into that spot in the puzzle
    def check_valid(self, x, y, v, grid):
        top_left_x, top_left_y = x//3*3, y//3*3
        return self.check_horizontal(y, v, grid) and self.check_vertical(x, v, grid) and self.check_square(top_left_x, top_left_y, v, grid)


    # find empty spot
    def find_empty(self, grid):
        for y in range(9):
            for x in range(9):
                if grid[y][x] == 0:
                    return y, x


    # solve the puzzle
    def solve(self, grid):
        empty = self.find_empty(grid)
        # base case
        if not empty:
            return True
        else:
            y, x = empty

        for v in range(1, 10):
            if self.check_valid(x, y, v, grid):
                grid[y][x] = v

                if self.solve(grid):
                    return True

                grid[y][x] = 0

        return False


    # print puzzle
    def print_puzzle(self, grid):
        output = ""
        for i in range(9):
            if i % 3 == 0 and not i == 0:
                output += "---------------------\n"
            for j in range(9):
                if j % 3 == 0 and not j == 0:
                    output += "| "
                output += (str(grid[i][j]) + " ")
            output += "\n"
        print(output)




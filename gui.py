import solve
import pygame
pygame.font.init()


class Grid:
    board = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    board_og = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    def __init__(self, rows, cols, width, height):
        self.rows = rows
        self.cols = cols
        self.cubes = [[Cube(self.board[i][j], i, j, width, height) for j in range(cols)] for i in range(rows)]
        self.width = width
        self.height = height
        self.model = None
        self.selected = None

    def update_model(self):
        self.model = [[self.cubes[i][j].value for j in range(self.cols)] for i in range(self.rows)]

    def place(self, val):
        row, col = self.selected
        self.cubes[row][col].set(val)
        self.update_model()
        self.board[row][col] = val

    def draw(self, win):
        # Draw Grid Lines
        gap = self.width / 9
        for i in range(self.rows+1):
            if i % 3 == 0 and i != 0:
                thick = 4
            else:
                thick = 1
            pygame.draw.line(win, (0,0,0), (0, i*gap), (self.width, i*gap), thick)
            pygame.draw.line(win, (0, 0, 0), (i * gap, 0), (i * gap, self.height), thick)

        # Draw Cubes
        for i in range(self.rows):
            for j in range(self.cols):
                self.cubes[i][j].draw(win)

        for i in range(9):
            for j in range(9):
                if self.board_og[i][j] != 0:
                    self.cubes[i][j].draw_red(win)

    def select(self, row, col):
        # Reset all other
        for i in range(self.rows):
            for j in range(self.cols):
                self.cubes[i][j].selected = False

        self.cubes[row][col].selected = True
        self.selected = (row, col)

    def clear(self):
        for i in range(len(self.cubes)):
            for j in range(len(self.cubes)):
                self.cubes[i][j].set(0)
                self.board[i][j] = 0
                self.board_og[i][j] = 0

    def click(self, pos):
        """
        :param: pos
        :return: (row, col)
        """
        if pos[0] < self.width and pos[1] < self.height:
            gap = self.width / 9
            x = pos[0] // gap
            y = pos[1] // gap
            return int(y), int(x)
        else:
            return None

    def is_finished(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.cubes[i][j].value == 0:
                    return False
        return True


class Cube:
    rows = 9
    cols = 9

    def __init__(self, value, row, col, width ,height):
        self.value = value
        self.row = row
        self.col = col
        self.width = width
        self.height = height
        self.selected = False
        self.blank = 0

    def draw(self, win):
        fnt = pygame.font.SysFont("comicsans", 40)

        gap = self.width / 9
        x = self.col * gap
        y = self.row * gap

        if self.value == 0:
            text = fnt.render("", 1, (0,0,0))
            win.blit(text, (x+5, y+5))
        elif self.value != 0:
            text = fnt.render(str(self.value), 1, (0, 0, 0))
            win.blit(text, (x + (gap/2 - text.get_width()/2), y + (gap/2 - text.get_height()/2)))

        if self.selected:
            pygame.draw.rect(win, (255,0,0), (x,y, gap ,gap), 3)

    def draw_red(self, win):
        fnt = pygame.font.SysFont("comicsans", 40)

        gap = self.width / 9
        x = self.col * gap
        y = self.row * gap

        if self.value != 0:
            text = fnt.render(str(self.value), 1, (255, 0, 0))
            win.blit(text, (x + (gap / 2 - text.get_width() / 2), y + (gap / 2 - text.get_height() / 2)))

    def set(self, val):
        self.value = val


def redraw_window(win, board):
    win.fill((255,255,255))
    # display controls
    fnt = pygame.font.SysFont("comicsans", 35)
    text = fnt.render("Controls:", 1, (0, 0, 0))
    win.blit(text, (20, 550))

    fnt = pygame.font.SysFont("comicsans", 20)
    text = fnt.render("Select - LEFT CLICK or ARROW KEYS", 1, (0, 0, 0))
    win.blit(text, (40, 580))

    text = fnt.render("Input Num - NUMBER KEY", 1, (0, 0, 0))
    win.blit(text, (40, 600))

    text = fnt.render("Delete - BACKSPACE", 1, (0, 0, 0))
    win.blit(text, (40, 620))

    text = fnt.render("Clear - C", 1, (0, 0, 0))
    win.blit(text, (40, 640))

    text = fnt.render("Solve - ENTER", 1, (0, 0, 0))
    win.blit(text, (40, 660))
    # Draw grid and board
    board.draw(win)


def main():
    win = pygame.display.set_mode((540,680))
    pygame.display.set_caption("Sudoku Solver")
    board = Grid(9, 9, 540, 540)
    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if not board.selected:
                    board.select(0,0)
                else:
                    i, j = board.selected

                if event.key == pygame.K_1 and (i or i ==0):
                    board.cubes[i][j].set(1)
                    board.place(board.cubes[i][j].value)
                if event.key == pygame.K_2 and (i or i ==0):
                    board.cubes[i][j].set(2)
                    board.place(board.cubes[i][j].value)
                if event.key == pygame.K_3 and (i or i ==0):
                    board.cubes[i][j].set(3)
                    board.place(board.cubes[i][j].value)
                if event.key == pygame.K_4 and (i or i ==0):
                    board.cubes[i][j].set(4)
                    board.place(board.cubes[i][j].value)
                if event.key == pygame.K_5 and (i or i ==0):
                    board.cubes[i][j].set(5)
                    board.place(board.cubes[i][j].value)
                if event.key == pygame.K_6 and (i or i ==0):
                    board.cubes[i][j].set(6)
                    board.place(board.cubes[i][j].value)
                if event.key == pygame.K_7 and (i or i ==0):
                    board.cubes[i][j].set(7)
                    board.place(board.cubes[i][j].value)
                if event.key == pygame.K_8 and (i or i ==0):
                    board.cubes[i][j].set(8)
                    board.place(board.cubes[i][j].value)
                if event.key == pygame.K_9 and (i or i ==0):
                    board.cubes[i][j].set(9)
                    board.place(board.cubes[i][j].value)
                if event.key == pygame.K_BACKSPACE:
                    board.place(board.cubes[i][j].blank)
                    board.board[i][j] = 0
                    board.board_og[i][j] = 0
                if event.key == pygame.K_c:
                    board.clear()
                if event.key == pygame.K_RETURN:
                    # keep track of original puzzle
                    for i in range(9):
                        for j in range(9):
                            board.board_og[i][j] = board.board[i][j]
                    solver = solve.Solver(board.board)
                    solver.solve(solver.puzzle)
                    solved = solver.puzzle
                    for i in range(9):
                        for j in range(9):
                            board.cubes[i][j].set(solved[i][j])

                if event.key == pygame.K_UP:
                    if board.selected[0] > 0:
                        board.select(board.selected[0] - 1, board.selected[1])
                if event.key == pygame.K_DOWN:
                    if board.selected[0] < 8:
                        board.select(board.selected[0] + 1, board.selected[1])
                if event.key == pygame.K_RIGHT:
                    if board.selected:
                        if board.selected[1] < 8:
                            board.select(board.selected[0], board.selected[1] + 1)
                if event.key == pygame.K_LEFT:
                    if board.selected:
                        if board.selected[1] > 0:
                            board.select(board.selected[0], board.selected[1] - 1)

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                clicked = board.click(pos)
                if clicked:
                    board.select(clicked[0], clicked[1])

        redraw_window(win, board)
        pygame.display.update()


if __name__ == "__main__":
    main()
pygame.quit()

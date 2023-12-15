import pygame
import random


class Board:
    def __init__(self, width, height):
        pygame.init()
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 30

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size



    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)

    def get_cell(self, mouse_pos):
        x = mouse_pos[0] - self.left
        y = mouse_pos[1] - self.top
        if x < 0 or y < 0:
            return None
        col = x // self.cell_size
        row = y // self.cell_size
        if col >= self.width or row >= self.height:
            return None
        else:
            return col, row

    def on_click(self, cell_coords):
        if cell_coords:
            self.board[cell_coords[1]][cell_coords[0]] = (self.board[cell_coords[1]][cell_coords[0]] + 1) % 3




class Minesweeper(Board):
    def __init__(self, width=10, height=10):
        super().__init__(width, height)
        self.board = [[10 if random.random() < 0.1 else -1 for _ in range(width)] for _ in range(height)]

    def render(self, screen):
        for row in range(self.height):
            for col in range(self.width):
                if self.board[row][col] == 10:
                    pygame.draw.rect(screen, "red",
                                     (self.left + self.cell_size * col, self.top + self.cell_size * row,
                                      self.cell_size, self.cell_size))
                pygame.draw.rect(screen, "white",
                                 (self.left + self.cell_size * col, self.top + self.cell_size * row,
                                  self.cell_size, self.cell_size), 1)
                if 0 <= self.board[row][col] <= 8:
                    font = pygame.font.Font(None, 20)
                    text = font.render(str(self.board[row][col]), True, '#00FF00')
                    screen.blit(text, (self.left + self.cell_size * col + 2, self.top + self.cell_size * row + 2))

    def on_click(self, cell_coords):
        if cell_coords:
            col, row = cell_coords
            if self.board[row][col] != 10:
                s = 0
                dx = ((-1, -1), (-1, 0), (-1, +1), (0, +1), (+1, +1), (+1, 0), (+1, -1), (0, -1))
                for d in dx:
                    if (0 <= row + d[0] < self.height and 0 <= col + d[1] < self.width and
                            self.board[row + d[0]][col + d[1]] == 10):
                        s += 1
            self.board[row][col] = s



if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Сапёр')
    size = width, height = 300, 300
    screen = pygame.display.set_mode(size)
    cell_size = 30
    game_Minesweeper = Minesweeper(width // cell_size, height // cell_size)
    game_Minesweeper.set_view(0, 0, cell_size)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                game_Minesweeper.get_click(event.pos)

        screen.fill((0, 0, 0))
        game_Minesweeper.render(screen)
        pygame.display.flip()
    pygame.quit()
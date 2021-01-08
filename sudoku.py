import math
import sys
import pygame
import pygame.key




class Sudoku(object):
    def __init__(self):
        self.ui = UI(self)
        self.screen = None
        self.regions = [[]] * 9
        self.cells = []
        self.selectedCell = None

        for i in range(9):
            for j in range(9):
                self.cells.append(Cell(self, math.floor(i / 3) * 3 + math.floor(j / 3), i, j))
                self.regions[math.floor(i / 3) * 3 + math.floor(j / 3)].append([self.cells[len(self.cells) - 1]])
        self.gameloop()

    def get_object_at(self, mouse):
        if(mouse[1] < self.screenSize[0]):
            square_x = math.floor(mouse[0] / (self.screenSize[0] / 9))
            square_y = math.floor(mouse[1] / (self.screenSize[0] / 9))
            print(square_x, square_y)
            return self.cells[square_y * 9 + square_x]
        else:
            pass

    def select_cell(self, cell):
        if(cell):
            if(self.selectedCell):
                self.selectedCell.deselect()
            self.selectedCell = cell
            cell.select()

    def set_number(self, number):
        if self.selectedCell:
            self.selectedCell.set_number(number)

    def gameloop(self):
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print("MouseDown")
                if event.type == pygame.MOUSEBUTTONUP:
                    print("MouseUp")
                    self.select_cell(self.get_object_at(pygame.mouse.get_pos()))

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DELETE or event.key == pygame.K_BACKSPACE or event.key == pygame.K_0:
                        self.set_number(0)
                    elif event.key == pygame.K_1:
                        self.set_number(1)
                    elif event.key == pygame.K_2:
                        self.set_number(2)
                    elif event.key == pygame.K_3:
                        self.set_number(3)
                    elif event.key == pygame.K_4:
                        self.set_number(4)
                    elif event.key == pygame.K_5:
                        self.set_number(5)
                    elif event.key == pygame.K_6:
                        self.set_number(6)
                    elif event.key == pygame.K_7:
                        self.set_number(7)
                    elif event.key == pygame.K_8:
                        self.set_number(8)
                    elif event.key == pygame.K_9:
                        self.set_number(9)
            self.draw()

class UI(object):
    def __init__(self, sudoku):
        self.screenSize = width, height = 600, 700
        pygame.init()
        font = pygame.font.SysFont('Tahoma', 60)
        chars = [
            font.render('1', True, (0, 0, 0)),
            font.render('2', True, (0, 0, 0)),
            font.render('3', True, (0, 0, 0)),
            font.render('4', True, (0, 0, 0)),
            font.render('5', True, (0, 0, 0)),
            font.render('6', True, (0, 0, 0)),
            font.render('7', True, (0, 0, 0)),
            font.render('8', True, (0, 0, 0)),
            font.render('9', True, (0, 0, 0))
        ]

        self.screen = pygame.display.set_mode(self.screenSize)
    def draw(self, sudoku):
        self.screen.fill((150, 150, 150))
        for cell in sudoku.cells:
            self.draw_cell(cell)
        pygame.display.flip()

    def draw_cell(self, cell):
        square_size = self.screenSize[0] / 9
        cell_x = square_size * cell.row
        cell_y = square_size * cell.col
        square = pygame.Rect(cell_x, cell_y, square_size, square_size)

        pygame.draw.rect(self.screen, (255, 255, 255), square, width=2, border_radius=2)

        if cell.number > 0:
            self.screen.blit(self.chars[cell.number-1], (cell_x, cell_y))


class Cell(object):
    def __init__(self, game, region, col, row):
        self.game = game
        self.region = region
        self.col = col
        self.row = row
        self.number = 0
        self.selected = False

    def select(self):
        self.selected = True

    def deselect(self):
        self.selected = False

    def set_number(self, number):
        self.number = number

newGame = Sudoku()
import math

import pygame
import pygame.key
import sys
print(sys.getrecursionlimit())



class Sudoku(object):
    def __init__(self):
        self.ui = UI()
        self.screen = None
        self.regions = [[] for rows in range(9)]
        self.rows = [[] for rows in range(9)]
        self.cols = [[] for rows in range(9)]

        self.cells = []
        self.selectedCell = None

        for i in range(9):
            for j in range(9):
                region_index = math.floor(i / 3) * 3 + math.floor(j / 3)
                self.cells.append(Cell(self, region_index, i, j))

                self.regions[region_index].append(self.cells[len(self.cells) - 1])

                self.rows[j].append(self.cells[len(self.cells) - 1])
                self.cols[i].append(self.cells[len(self.cells) - 1])
        self.gameloop()


    def get_object_at(self, mouse):
        if mouse[1] < self.ui.screenSize[0]:
            square_x = math.floor(mouse[0] / (self.ui.screenSize[0] / 9))
            square_y = math.floor(mouse[1] / (self.ui.screenSize[0] / 9))
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
            if self.is_safe(self.selectedCell, number):
                self.selectedCell.set_number(number)

    def gameloop(self):
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pass
                if event.type == pygame.MOUSEBUTTONUP:
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
                    elif event.key == pygame.K_SPACE:
                        self.solve()
            self.ui.draw(self)

    def is_safe(self, cell, number):
        if number == 0:
            return True

        for i in self.regions[cell.region]:
            if number == i.number:
                return False

        for i in self.rows[cell.row]:
            if number == i.number:
                return False

        for i in self.cols[cell.col]:
            if number == i.number:
                return False
        return True

    def find_unassigned(self):
        for cell in self.cells:
            if cell.number == 0:
                return cell
        return False

    def solve(self):
        cell = self.find_unassigned()

        if cell:
            for num in range(9):
                if self.is_safe(cell, num+1):
                    cell.set_number(num+1)
                    check = self.solve()
                    if check:
                        return True
                    else:
                        cell.set_number(0)

            return False
        else:
            return True
class UI(object):
    def __init__(self):
        self.screenSize = width, height = 600, 700
        pygame.init()
        font = pygame.font.SysFont('Tahoma', 60)
        self.chars = [
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
        if cell.selected:
            pygame.draw.rect(self.screen, (255, 255, 255), square, border_radius=2)
        else:
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
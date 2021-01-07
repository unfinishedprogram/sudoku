import math
import sys
import pygame
import pygame.key


class Sudoku(object):
    def __init__(self):
        # initalize UI
        pygame.init()

        size = width, height = 320, 240
        speed = [2, 2]
        black = 0, 0, 0

        screen = pygame.display.set_mode(size)

        ball = pygame.image.load("intro_ball.gif")
        ballrect = ball.get_rect()

        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()

            ballrect = ballrect.move(speed)
            if ballrect.left < 0 or ballrect.right > width:
                speed[0] = -speed[0]
            if ballrect.top < 0 or ballrect.bottom > height:
                speed[1] = -speed[1]

            screen.fill(black)
            screen.blit(ball, ballrect)
            pygame.display.flip()

        self.regions = [[]] * 9
        self.cells = []
        for i in range(9):
            for j in range(9):
                self.cells.append(Cell(self, math.floor(i / 3) * 3 + math.floor(j / 3), i, j))
                self.regions[math.floor(i / 3) * 3 + math.floor(j / 3)].append([self.cells[len(self.cells) - 1]])

    def print(self):
        index = 0
        for cell in self.cells:
            if (index > 8):
                index = 0
                print()
            print(cell.number, end='')
            index += 1


class Cell(object):
    def __init__(self, game, region, col, row):
        self.game = game
        self.region = region
        self.col = col
        self.row = row
        self.number = 0


game = Sudoku()
game.print()

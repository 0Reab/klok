import random
import time
import pygame
from pygame.locals import *

SIZE = 40
BACKGROUND_COLOR = (110, 110, 5)
BOARD = ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8']

class Game:
    def __init__(self):
        pygame.init()

        pygame.mixer.init()
        self.surface = pygame.display.set_mode((1000, 900))
        #self.squares = Squares(self.surface, 1)
    def run(self):
        running = True
        pause = False
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_RETURN:
                        pause = False

                    #if not pause:
                        #if event.key == K_UP:
                            #self.piece.move_up()

                elif event.type == QUIT:
                    running = False

if __name__ == "__main__":
    game = Game()
    game.run()


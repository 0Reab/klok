import pygame
from pygame.locals import *

class Game:
    def __init__(self):
        pygame.init()

        pygame.mixer.init()
        self.surface = pygame.display.set_mode((1000, 900))
        # self.squares = Squares(self.surface, 1)

    def run(self):
        running = True
        pause = False
        while running:
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_RETURN:
                        pause = False

                    # if not pause:
                    # if event.key == K_UP:
                    # self.piece.move_up()

                elif event.type == QUIT:
                    running = False

class X:
    def __init__(self):
        pygame.init()

    def

if __name__ == "__main__":
    game = Game()
    game.run()

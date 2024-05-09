import pygame
import sys
from pygame.locals import *

class Game():
    def __init__(self, WINDOW_SIZE = (16*50, 16*50), FPS = 60) -> None:
        pygame.init()
        self.WINDOW_SIZE = WINDOW_SIZE
        self.screen:pygame.surface = pygame.display.set_mode(WINDOW_SIZE)
        self.clock = pygame.time.Clock()
        self.FPS = FPS
        self.main()
    
    def main(self):
        while (True):
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()
            self.clock.tick(self.FPS)
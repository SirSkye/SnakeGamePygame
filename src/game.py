import pygame
import sys
from pygame.locals import *
from snake import Snake
from apple import Apple
from utils import load_img
from typing import Tuple

class Game():
    def __init__(self, TILES:Tuple[int, int], FPS:int = 60) -> None:
        pygame.init()
        pygame.display.set_caption("Snake Game")
        self.TILES = TILES
        self.WINDOW_SIZE = (TILES[0] * 50, TILES[1] * 50)
        self.screen:pygame.surface = pygame.display.set_mode(self.WINDOW_SIZE)
        self.clock = pygame.time.Clock()
        self.FPS = FPS
        self.apple = Apple()
        self.snake = Snake()

        assets_path = r"../assets"
        self.grass_light = load_img(fr"{assets_path}/grass_light.png")
        self.grass_dark = load_img(fr"{assets_path}/grass_dark.png")
        self.main()
    
    def main(self):
        while (True):
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            self.draw_grass()
            self.snake.draw_snake(self.screen) 
            pygame.display.update()
            self.clock.tick(self.FPS)

    def draw_grass(self):
        for y in range(0, self.TILES[1]):
            init_color = 0 if (y % 2 == 0) else 1
            for x in range(0, self.TILES[0]):
                base_rect = pygame.Rect(x*50, y*50, 50, 50)
                if (init_color % 2 == 0):
                    self.screen.blit(self.grass_dark, base_rect)
                else:
                    self.screen.blit(self.grass_light, base_rect)
                init_color += 1
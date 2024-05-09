import pygame
import sys
from pygame.locals import *
from snake import Snake
from apple import Apple
from utils import load_img
from typing import Tuple
from pygame.math import Vector2

class Game():
    def __init__(self, TILES:Tuple[int, int], FPS:int = 60) -> None:
        pygame.init()
        pygame.display.set_caption("Snake Game")

        self.UPDT_SCREEN = pygame.USEREVENT
        pygame.time.set_timer(self.UPDT_SCREEN, 300)

        self.TILES = TILES
        self.WINDOW_SIZE = (TILES[0] * 50, TILES[1] * 50)
        self.screen:pygame.surface = pygame.display.set_mode(self.WINDOW_SIZE)
        self.clock = pygame.time.Clock()
        self.FPS = FPS
        self.snake = Snake()
        self.apple = Apple(self.snake.body)

        assets_path = r"../assets"
        self.grass_light = load_img(fr"{assets_path}/grass_light.png")
        self.grass_dark = load_img(fr"{assets_path}/grass_dark.png")
        self.main()
    
    def main(self) -> None:
        while (True):
            for event in pygame.event.get():
                if event.type == self.UPDT_SCREEN:
                    self.update()
                elif event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_UP:
                        if self.snake.dir != Vector2(0, 1):
                            self.snake.dir = Vector2(0, -1)
                    elif event.key == K_DOWN:
                        if self.snake.dir != Vector2(0, -1):
                            self.snake.dir = Vector2(0, 1)
                    elif event.key == K_LEFT:
                        if self.snake.dir != Vector2(1, 0):
                            self.snake.dir = Vector2(-1, 0)
                    elif event.key == K_RIGHT:
                        if self.snake.dir != Vector2(-1, 0):
                            self.snake.dir = Vector2(1, 0)

            self.draw_grass()
            self.apple.draw(self.screen)
            self.snake.draw(self.screen) 
            pygame.display.update()

            self.clock.tick(self.FPS)

    def draw_grass(self) -> None:
        for y in range(0, self.TILES[1]):
            init_color = 0 if (y % 2 == 0) else 1
            for x in range(0, self.TILES[0]):
                base_rect = pygame.Rect(x*50, y*50, 50, 50)
                if (init_color % 2 == 0):
                    self.screen.blit(self.grass_dark, base_rect)
                else:
                    self.screen.blit(self.grass_light, base_rect)
                init_color += 1
    
    def update(self) -> None:
        apple_collected =self.check_collision()
        self.snake.move()
        if apple_collected:
            self.apple.generate_position(self.snake.body)
        self.check_fail()
    
    def check_collision(self) -> bool:
        if (self.snake.body[0] == self.apple.position):
            self.snake.add_new()
            return True
        return False
    
    def check_fail(self) -> bool:
        for body in self.snake.body[1:]:
            if body == self.snake.body[0]:
                print("failed")
                pygame.quit()
                sys.exit()
                return True
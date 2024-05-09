import pygame
from pygame.math import Vector2
from pygame.locals import *
from utils import load_img

class Snake():
    def __init__(self) -> None:
        self.body = [Vector2(6, 4), Vector2(5, 4), Vector2(4, 4)]
        self.dir = Vector2(1, 0)
        self.length = 3

        assets_path = r"..\assets"
        self.head_img = load_img(fr"{assets_path}\snake_head.png")
        self.body_img = load_img(fr"{assets_path}\snake_body.png")
        self.twist_img = load_img(fr"{assets_path}\snake_twist.png")
        self.tail_img = load_img(fr"{assets_path}\snake_tail.png")
    
    def draw_snake(self, screen:pygame.Surface):
        TILE_SIZE = 50
        for index, body in enumerate(self.body):
            base_rect = pygame.Rect(body.x * TILE_SIZE, body.y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
            if index == 0:
                screen.blit(self.head_img, base_rect)
            elif index ==self.length - 1:
                screen.blit(self.tail_img, base_rect)
            else:
                screen.blit(self.body_img, base_rect)
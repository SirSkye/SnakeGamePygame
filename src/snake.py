import pygame
from pygame.math import Vector2
from pygame.locals import *
from utils import load_img

class Snake():
    def __init__(self) -> None:
        self.head = Vector2(4, 4)
        self.body = [Vector2(4, 5), Vector2(4, 6)]
        self.dir = Vector2(1, 0)

        assets_path = r"..\assets"
        self.head_img = load_img(fr"{assets_path}\snake_head.png")
        self.body_img = load_img(fr"{assets_path}\snake_body.png")
        self.twist_img = load_img(fr"{assets_path}\snake_twist.png")
        self.tail_img = load_img(fr"{assets_path}\snake_tail.png")
    
    def draw_snake(self, screen:pygame.Surface):
        TILE_SIZE = 50
        base_rect = pygame.Rect(self.head.x * TILE_SIZE, self.head.y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
        screen.blit(self.head_img, base_rect)
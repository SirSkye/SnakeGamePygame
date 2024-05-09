from random import randint
from typing import List, Tuple

import pygame
from pygame.locals import *
from pygame.math import Vector2

from utils import load_img


class Apple():
    def __init__(self, snake_pos: List[pygame.Vector2]) -> None:
        self.generate_position(snake_pos)

        assets_path = r"../assets"
        self.apple_img = load_img(fr"{assets_path}/apple.png")
        
    
    #very inefficnet
    def generate_position(self, snake_pos: List[pygame.Vector2]) -> None:
        while (True):
            candidate = Vector2(randint(0, 16-1), randint(0, 16-1))
            if candidate not in snake_pos:
                self.position = candidate
                break
    
    def draw(self, screen: pygame.Surface):
        TILE_SIZE = 50
        base_rect = pygame.Rect(self.position.x * TILE_SIZE, self.position.y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
        screen.blit(self.apple_img, base_rect)
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

        base_img = load_img(fr"{assets_path}\snake_head.png")
        self.head_imgs = list()
        self.head_imgs.append(base_img) #UP
        self.head_imgs.append(pygame.transform.rotate(base_img, 90)) #Left
        self.head_imgs.append(pygame.transform.rotate(base_img, 180)) #Down
        self.head_imgs.append(pygame.transform.rotate(base_img, 270)) #Right

        self.body_img = load_img(fr"{assets_path}\snake_body_seg.png")

    def move(self) -> None:
        for x in range(self.length):
            self.body[x] += self.dir
    
    def draw(self, screen:pygame.Surface) -> None:
        TILE_SIZE = 50
        for index, body in enumerate(self.body):
            base_rect = pygame.Rect(body.x * TILE_SIZE, body.y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
            if index == 0:
                screen.blit(self.generate_end_img(self.dir), base_rect)
            else:
                screen.blit(self.body_img, base_rect)

    def generate_end_img(self, dir: Vector2) -> pygame.Surface:
        if (dir == Vector2(1, 0)): return self.head_imgs[3] #Right
        if (dir == Vector2(-1, 0)): return self.head_imgs[1] #Left
        if (dir == Vector2(0, 1)): return self.head_imgs[0] #Up
        return self.head_imgs[2]
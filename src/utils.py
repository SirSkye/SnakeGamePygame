import pygame

def load_img(path: str) -> pygame.Surface:
    return pygame.image.load(path).convert_alpha()
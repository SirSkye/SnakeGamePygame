import pygame

class BaseScreen:
    def __init__(self, name, app):
        self.name = name
        self.app = app

    def handle_events(self, event:pygame.event.Event) -> None:
        pass

    def update(self) -> None:
        pass

    def draw(self) -> None:
        pass

class ScreenManager:
    def __init__(self, app) -> None:
        self.app = app
        self.screens = dict()
        self.screen = None
    
    def add_screen(self, screen):
        self.screens[screen.name] = screen
    
    def set_screen(self, name):
        self.screen = self.screens[name]
    
    def update(self):
        self.screen.update()
    
    def draw(self):
        self.screen.draw()
    
    def handle_events(self, event):
        self.screen.handle_events(event)
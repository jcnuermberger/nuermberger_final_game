import pygame
from game_parameters import *

class Bottle(pygame.sprite.Sprite):
    def __init__(self, shelf_num, x, y):
        super().__init__()
        self.image = pygame.image.load("../assets/sprites/bottle.png").convert()
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.shelf_num = shelf_num
        self.x = x
        self.y = y
        self.rect.x = self.x
        self.rect.y = self.y
        self.speed = 5

    def update(self):
        self.y += self.speed
        if self.y >= SCREEN_HEIGHT - (187 + 125*(self.shelf_num-1)):
            self.y = SCREEN_HEIGHT - (187 + 125 * (self.shelf_num - 1))
        self.rect.y = self.y
    def draw(self, screen):
        screen.blit(self.image, self.rect)
bottles = pygame.sprite.Group()

class Chicken(pygame.sprite.Sprite):
    def __init__(self, shelf_num, x, y):
        super().__init__()
        self.image = pygame.image.load("../assets/sprites/chicken.png").convert()
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()
        self.shelf_num = shelf_num
        self.x = x
        self.y = y
        self.rect.x = self.x
        self.rect.y = self.y
        self.speed = 5
    def update(self):
        self.y += self.speed
        if self.y >= SCREEN_HEIGHT - (187 + 125*(self.shelf_num)):
            self.y = SCREEN_HEIGHT - (self.image.get_height() + 125*(self.shelf_num))
        self.rect.y = self.y
    def draw(self, screen):
        screen.blit(self.image, self.rect)
chickens = pygame.sprite.Group()
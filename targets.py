import pygame
from game_parameters import *

class Bottle(pygame.sprite.Sprite):
    def __init__(self, shelf_num):
        super().__init__()
        self.image = pygame.image.load("../assets/sprites/bottle.png").convert()
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.shelf_num = shelf_num
        self.rect.x = SCREEN_WIDTH - 40
        self.rect.y = SCREEN_HEIGHT - (187 + 125*(shelf_num-1))
        # self.rect = ((SCREEN_WIDTH - 40), (SCREEN_HEIGHT - (187 + 125*(shelf_num-1))))
    def draw(self, screen):
        screen.blit(self.image, self.rect)
bottles = pygame.sprite.Group()

class Chicken(pygame.sprite.Sprite):
    def __init__(self, shelf_num):
        super().__init__()
        self.image = pygame.image.load("../assets/sprites/chicken.png").convert()
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()
        self.shelf_num = shelf_num
        self.rect.x = SCREEN_WIDTH - self.image.get_width()/1.5
        self.rect.y = SCREEN_HEIGHT - (self.image.get_height() + 125*(shelf_num))
    def draw(self, screen):
        screen.blit(self.image, self.rect)
chickens = pygame.sprite.Group()
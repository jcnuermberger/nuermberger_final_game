import pygame
from game_parameters import *
# load sprites
# chicken = pygame.image.load("../assets/sprites/chicken.png").convert()
class Bottle(pygame.sprite.Sprite):
    def __init__(self, shelf_num):
        super().__init__()
        self.image = pygame.image.load("../assets/sprites/bottle.png").convert()
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.shelf_num = shelf_num
        self.rect = ((SCREEN_WIDTH - 40), (SCREEN_HEIGHT - (187+ 125*(shelf_num-1) )))
    def draw(self, screen, shelf_num=1):
        screen.blit(self.image, self.rect)
bottles = pygame.sprite.Group()


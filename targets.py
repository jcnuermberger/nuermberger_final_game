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
    def update(self):
        self.y += 100
        self.rect.y = self.y
    def draw(self, screen, shelf_num=1):
        self.rect = ((SCREEN_WIDTH - 40), (SCREEN_HEIGHT - (187+125(shelf_num-1))))
        screen.blit(self.image, self.rect)
bottles = pygame.sprite.Group()


class Fish(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("../assets/sprites/green_fish.png").convert()
        self.image = pygame.transform.flip(self.image, True, False)
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.center = (x,y)
        # self.speed = random.uniform(MIN_SPEED,MAX_SPEED)
    def update(self):
        self.x -= self.speed
        self.rect.x = self.x
    def draw(self, screen):
        screen.blit(self.image, self.rect)
fishes = pygame.sprite.Group()

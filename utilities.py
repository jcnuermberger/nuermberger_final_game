import pygame
import random
from game_parameters import*
from bullet import Bullet, bullets
from targets import Bottle, bottles, Chicken, chickens


def draw_background(surf):
    # load fonts
    main_font = pygame.font.Font("../assets/fonts/main_font.ttf", 48)
    title = main_font.render("Shootin' Saloon", True, (0,0,0))
    # Load tiles from assets to surfaces
    sand_top = pygame.image.load("../assets/sprites/sand_top.png").convert()
    saloon = pygame.image.load("../assets/sprites/saloon.png").convert()
    cloud = pygame.image.load("../assets/sprites/cloud.png").convert()
    shelf = pygame.image.load("../assets/sprites/shelf.png").convert()
    cowboy = pygame.image.load("../assets/sprites/cowboy.png").convert()
    bottle = pygame.image.load("../assets/sprites/bottle.png").convert()
    # Use the png transparency
    sand_top.set_colorkey((0, 0, 0))
    saloon.set_colorkey(((255, 255, 255)))
    cloud.set_colorkey((255, 255, 255))
    shelf.set_colorkey((255, 255, 255))
    cowboy.set_colorkey((255, 255, 255))
    bottle.set_colorkey((255,255,255))

    # make the screen
    surf.fill((190, 250, 255))
    for x in range(0, SCREEN_WIDTH, sand_top.get_width()):
        for y in range(550, SCREEN_HEIGHT, sand_top.get_height()):
            surf.blit(sand_top, (x, y))
    surf.blit(saloon, (200, SCREEN_HEIGHT - saloon.get_height()))
    for x in range(0, SCREEN_WIDTH, cloud.get_width()):
        pos = random.randint(0, SCREEN_WIDTH)
        surf.blit(cloud, (pos, 0))
    for i in range (4):
        surf.blit(shelf, (SCREEN_WIDTH - shelf.get_width()/3,SCREEN_HEIGHT- i*125))
    surf.blit(cowboy, (0,SCREEN_HEIGHT - (cowboy.get_height()+sand_top.get_height()/2)))
    surf.blit(title, (SCREEN_WIDTH/2-title.get_width()/2,0))

def draw_menu(surf):
    # load fonts
    main_font = pygame.font.Font("../assets/fonts/main_font.ttf", 48)
    title = main_font.render("Shootin' Saloon", True, (0, 0, 0))
    # Load tiles from assets to surfaces
    sand_top = pygame.image.load("../assets/sprites/sand_top.png").convert()
    cloud = pygame.image.load("../assets/sprites/cloud.png").convert()
    scroll = pygame.image.load("../assets/sprites/scroll.png").convert()
    # Use the png transparency
    scroll.set_colorkey((255,255,255))
    sand_top.set_colorkey((0, 0, 0))
    cloud.set_colorkey((255, 255, 255))

    # make the screen
    surf.fill((190, 250, 255))
    for x in range(0, SCREEN_WIDTH, sand_top.get_width()):
        for y in range(550, SCREEN_HEIGHT, sand_top.get_height()):
            surf.blit(sand_top, (x, y))
    for x in range(0, SCREEN_WIDTH, cloud.get_width()):
        pos = random.randint(0, SCREEN_WIDTH)
        surf.blit(cloud, (pos, 0))
    surf.blit(scroll, (SCREEN_WIDTH / 2 - scroll.get_width() / 2, 0))
    surf.blit(title, (SCREEN_WIDTH / 2 - title.get_width() / 2, 0))

def add_bullets(num_bullet, pos, angle):
    for _ in range(num_bullet):
        bullets.add(Bullet(pos[0],pos[1], angle))
def add_bottles(shelf_num):
    bottles.add(Bottle(shelf_num))
def add_chickens(shelf_num):
    chickens.add(Chicken(shelf_num))
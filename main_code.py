import pygame
import sys
from game_parameters import *
from utilities import draw_background, add_bullets, add_bottles
from bullet import bullets
from targets import bottles

pygame.init()

# make the screen dimensions
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Shootin' Saloon")
background = screen.copy()
draw_background(background)
# initialize fonts
main_font = pygame.font.Font("../assets/fonts/main_font.ttf", 100)
# initialize variables
angle = 0
# intialize timer
clock = pygame.time.Clock()
counter = 10
text = main_font.render(str(counter), True, (0,0,0))
timer_event = pygame.USEREVENT+1
pygame.time.set_timer(timer_event, 1000)

# initialize sounds
gunshot = pygame.mixer.Sound("../assets/sounds/gunshot.mp3")
bottle_break = pygame.mixer.Sound("../assets/sounds/bottle_break.mp3")
background_music = pygame.mixer.Sound('../assets/sounds/background.mp3')
bottle = pygame.image.load("../assets/sprites/bottle.png").convert()
bottle.set_colorkey((255,255,255))

# add target sprites
add_bottles(1)
add_bottles(2)
add_bottles(3)
# main loop
running = True
while running:
    # set frame speed
    clock.tick(60)
    pygame.mixer.Sound.play(background_music)
    for event in pygame.event.get():
        if event.type == pygame.event.get():
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                angle -= .035
            if event.key == pygame.K_DOWN:
                angle += .035
            if event.key == pygame.K_SPACE:
                pos = (100,450)
                add_bullets(1, pos, angle)
                pygame.mixer.Sound.play(gunshot)
        elif event.type == timer_event:
            counter -= 1
            text = main_font.render(str(counter), True, (0,0,0))
            if counter == 0:
                running = False
    # draw the background
    screen.blit(background, (0, 0))

    # draw timer
    screen.blit(text, (10,0))

    # update objects
    bullets.update()

    # draw objects
    for bullet in bullets:
        bullet.draw_bullet(screen)

    # draw bottles on shelves
    for bottle in bottles:
        bottles.draw(screen, bottle.shelf_num)

     # results for bullets
    for bullet in bullets:
        if bullet.rect.x > SCREEN_WIDTH:
            bullets.remove(bullet)
        for bottle in bottles:
            bullet_bottle = pygame.sprite.spritecollide(bullet, bottles, True)
            if bullet_bottle:
                counter += 5
                bottles.remove(bottle)
                add_bottles(bottle.shelf_num)
                bullets.remove(bullet)
                pygame.mixer.Sound.play(bottle_break)

    pygame.display.flip()
pygame.quit()
sys.exit()
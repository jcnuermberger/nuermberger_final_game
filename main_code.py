import pygame
import sys
import random
import time
from game_parameters import *
from utilities import draw_background, draw_menu, add_bullets, add_bottles, add_chickens
from bullet import bullets
from targets import bottles, chickens
pygame.init()

# make the screen dimensions
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Shootin' Saloon")
background = screen.copy()
draw_background(background)
# initialize fonts
main_font = pygame.font.Font("../assets/fonts/main_font.ttf", 50)
welcome_font = pygame.font.Font("../assets/fonts/main_font.ttf", 20)

# initialize variables
angle = 0
# intialize timer
clock = pygame.time.Clock()
counter = 25
text = main_font.render(f"T:{str(counter)}", True, (0,0,0))
timer_event = pygame.USEREVENT+1
pygame.time.set_timer(timer_event, 1000)
# initialize score
score = 0
score_text = main_font.render(f"S:{str(score)}", True, (0,0,0))

# initialize sounds
gunshot = pygame.mixer.Sound("../assets/sounds/gunshot.mp3")
bottle_break = pygame.mixer.Sound("../assets/sounds/bottle_break.mp3")
chicken_death = pygame.mixer.Sound("../assets/sounds/chicken_death.mp3")
background_music = pygame.mixer.Sound("../assets/sounds/background.mp3")
scroll = pygame.image.load("../assets/sprites/scroll.png").convert()
scroll.set_colorkey((255,255,255))

# add target sprites
add_bottles(1)
add_bottles(2)
add_bottles(3)

# main loop
running = True
while running:
    draw_menu(screen)
    line2 = welcome_font.render("Your goal is to survive for as long", True, (0,0,0))
    line3 = welcome_font.render("as possible and reach the highest score.", True, (0,0,0))
    line4 = welcome_font.render("Each bottle you break will give you +1 ", True, (0,0,0))
    line5 = welcome_font.render("score and 3 more seconds of survival,", True, (0,0,0))
    line6 = welcome_font.render("but every chicken you shoot gives you", True, (0,0,0))
    line7 = welcome_font.render("-1 score and you lose 2 seconds of life.", True, (0,0,0))
    line8 = welcome_font.render("Good Luck!", True, (0,0,0))
    screen.blit(line2, (SCREEN_WIDTH / 2 - line2.get_width() / 2,  100))
    screen.blit(line3, (SCREEN_WIDTH / 2 - line3.get_width() / 2, 150))
    screen.blit(line4, (SCREEN_WIDTH / 2 - line4.get_width() / 2, 200))
    screen.blit(line5, (SCREEN_WIDTH / 2 - line5.get_width() / 2, 250))
    screen.blit(line6, (SCREEN_WIDTH / 2 - line6.get_width() / 2, 300))
    screen.blit(line7, (SCREEN_WIDTH / 2 - line7.get_width() / 2, 350))
    screen.blit(line8, (SCREEN_WIDTH / 2 - line8.get_width() / 2, 400))
    pygame.display.flip()
    time.sleep(10)
    running = False

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
                angle -= .05
            if event.key == pygame.K_DOWN:
                angle += .05
            if event.key == pygame.K_SPACE:
                pos = (100,450)
                add_bullets(1, pos, angle)
                # pygame.mixer.Sound.play(gunshot)
        elif event.type == timer_event:
            counter -= 1
            text = main_font.render(f"T:{str(counter)}", True, (0,0,0))
            if counter <= 0:
                running = False
    # draw the background
    screen.blit(background, (0, 0))

    # draw timer and score
    screen.blit(text, (0,0))
    screen.blit(score_text, (0, 40))

    # update objects
    bullets.update()

    # draw objects
    for bullet in bullets:
        bullet.draw_bullet(screen)

    # draw bottles/chickens on shelves
    for bottle in bottles:
        bottles.draw(screen, bottle.shelf_num)
    for chicken in chickens:
        chickens.draw(screen, chicken.shelf_num)

     # results for bullets
    for bullet in bullets:
        if bullet.rect.x > SCREEN_WIDTH:
            bullets.remove(bullet)
        for bottle in bottles:
            bullet_bottle = pygame.sprite.spritecollide(bullet, bottles, True)
            number_shelf = bottle.shelf_num
            if bullet_bottle:
                counter += 3
                score += 1
                score_text = main_font.render(f"S:{str(score)}", True, (0, 0, 0))
                bottles.remove(bottle)
                bullets.remove(bullet)
                pygame.mixer.Sound.play(bottle_break)
                num = random.randint(1,3)
                if num == 1:
                    add_chickens(number_shelf)
                else:
                    add_bottles(number_shelf)
        for chicken in chickens:
            bullet_chicken = pygame.sprite.spritecollide(bullet, chickens, True)
            number_shelf = chicken.shelf_num
            if bullet_chicken:
                counter -= 2
                score -= 1
                score_text = main_font.render(f"S:{str(score)}", True, (0, 0, 0))
                chickens.remove(chicken)
                bullets.remove(bullet)
                pygame.mixer.Sound.play(chicken_death)
                num = random.randint(1, 3)
                if num == 1:
                    add_chickens(number_shelf)
                else:
                    add_bottles(number_shelf)
    pygame.display.flip()


screen.blit(background, (0, 0))
screen.blit(scroll, (SCREEN_WIDTH / 4 - score_text.get_width() / 2,0))
# show a game over message
message = main_font.render("Game Over", True, (0, 0, 0))
screen.blit(message, (SCREEN_WIDTH / 2 - message.get_width() / 2, SCREEN_HEIGHT / 2 -message.get_height() / 2))
# show the final score
score_text = main_font.render(f"Score: {score}", True, (0, 0, 0))
screen.blit(score_text, (SCREEN_WIDTH / 2 - score_text.get_width() / 2,SCREEN_HEIGHT / 2 + message.get_height()))


pygame.display.flip()

# play game over sound effect
# pygame.mixer.Sound.play(bubbles)
# wait for user to exit the game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Quit Pygame
            pygame.quit()
            sys.exit()
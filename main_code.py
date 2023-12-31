import pygame
import sys
import random
import time
from game_parameters import *
from utilities import draw_background, draw_menu, add_bullets, add_bottles, add_chickens, load_high_score, save_high_score
from bullet import bullets
from targets import bottles, chickens
pygame.init()

# make the screen
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
counter = 23
text = main_font.render(f"T:{str(counter)}", True, (0,0,0))
timer_event = pygame.USEREVENT+1
pygame.time.set_timer(timer_event, 1000)

# initialize score
score = 0
score_text = main_font.render(f"S:{str(score)}", True, (0,0,0))
high_score = load_high_score()


# initialize sounds and menu tile
gunshot = pygame.mixer.Sound("../assets/sounds/gunshot.mp3")
bottle_break = pygame.mixer.Sound("../assets/sounds/bottle_break.mp3")
chicken_death = pygame.mixer.Sound("../assets/sounds/chicken_death.mp3")
background_music = pygame.mixer.Sound("../assets/sounds/background.mp3")
scroll = pygame.image.load("../assets/sprites/scroll.png").convert()
scroll.set_colorkey((255,255,255))

# add target sprites
for i in range(1,4):
    add_bottles(i)

# main loop
running = True
while running:
    draw_menu(screen)
    # display welcome message and instructions
    line2 = welcome_font.render("Your goal is to survive for as long", True, (0,0,0))
    line3 = welcome_font.render("as possible and reach the highest score.", True, (0,0,0))
    line4 = welcome_font.render("Each bottle you break will give you +1 ", True, (0,0,0))
    line5 = welcome_font.render("score and 3 more seconds of survival,", True, (0,0,0))
    line6 = welcome_font.render("but every chicken you shoot gives you", True, (0,0,0))
    line7 = welcome_font.render("-1 score and you lose 4 seconds of life.", True, (0,0,0))
    line8 = welcome_font.render(f"Can you beat the high score: {high_score}", True, (0,0,0))
    line9 = welcome_font.render("Good Luck!", True, (0,0,0))
    screen.blit(line2, (SCREEN_WIDTH / 2 - line2.get_width() / 2,  100))
    screen.blit(line3, (SCREEN_WIDTH / 2 - line3.get_width() / 2, 150))
    screen.blit(line4, (SCREEN_WIDTH / 2 - line4.get_width() / 2, 200))
    screen.blit(line5, (SCREEN_WIDTH / 2 - line5.get_width() / 2, 250))
    screen.blit(line6, (SCREEN_WIDTH / 2 - line6.get_width() / 2, 300))
    screen.blit(line7, (SCREEN_WIDTH / 2 - line7.get_width() / 2, 350))
    screen.blit(line8, (SCREEN_WIDTH / 2 - line8.get_width() / 2, 400))
    screen.blit(line9, (SCREEN_WIDTH / 2 - line9.get_width() / 2, 450))
    pygame.display.flip()
    # give time to read
    time.sleep(8)
    running = False

running = True
pygame.mixer.Sound.play(background_music)
while running:
    # set frame speed
    clock.tick(60)

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
                pygame.mixer.Sound.play(gunshot)
        elif event.type == timer_event: #timer loop
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
    bottles.update()
    chickens.update()

    # draw objects
    for bullet in bullets:
        bullet.draw_bullet(screen)
    for bottle in bottles:
        bottles.draw(screen, bottle.shelf_num)
    for chicken in chickens:
        chickens.draw(screen, chicken.shelf_num)

    # results for bullets
    for bullet in bullets:
        if bullet.rect.x > SCREEN_WIDTH:
            bullets.remove(bullet)
        for bottle in bottles:
            bullet_bottle = bottle.rect.colliderect(bullet)
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
            bullet_chicken = chicken.rect.colliderect(bullet)
            number_shelf = chicken.shelf_num
            if bullet_chicken:
                counter -= 4
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



# game over screen
screen.blit(background, (0, 0))
# extract high score
if score > high_score:
    high_score = score
    save_high_score(high_score)
screen.blit(scroll, (SCREEN_WIDTH / 4 - score_text.get_width() / 2,0))
# show a game over message
message = main_font.render("Game Over", True, (0, 0, 0))
screen.blit(message, (SCREEN_WIDTH / 2 - message.get_width() / 2, SCREEN_HEIGHT / 2 -message.get_height() / 2))
# show the final score
score_text = main_font.render(f"Your score: {score}", True, (0, 0, 0))
screen.blit(score_text, (SCREEN_WIDTH / 2 - score_text.get_width() / 2,SCREEN_HEIGHT / 4 + message.get_height()))
high_score_text = main_font.render(f"The high score: {high_score}", True, (0,0,0))
screen.blit(high_score_text, (SCREEN_WIDTH / 1.4 - high_score_text.get_width(), SCREEN_HEIGHT/1.5 - high_score_text.get_height()))

pygame.display.flip()

# exit pygame
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
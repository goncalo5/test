#!/usr/bin/env python
import random
import pygame
import os
pygame.init()

# SETTINGS
# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (200, 0, 0)
GREEN = (0, 200, 0)
BLUE = (0, 0, 255)
bright_RED = (255, 0, 0)
bright_GREEN = (0, 255, 0)

# Screen
display_width = 800
display_height = 800

BACKGROUD_COLOR = BLACK

FPS = 60

# Text
TEXT_COLOR = WHITE

# music:
MUSIC_GAME = "music/Rize_Up.mp3"
CRASH_SOUND = "music/car_door.wav"

# car
car_width = 128
car_height = 128
car_margin = 40
car_init_vel = 1000

# things:
thing_width = 100
thing_height = 100
THINGS_COLOR = BLUE
thing_init_speed = 500
THINGS_ACCELERATION = 20

# Buttons:
BUTTON_WIDTH = 120
BUTTON_HEIGHT = 50

is_paused = False

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("A bit Racey")
clock = pygame.time.Clock()


try:
    carImg = pygame.image.load(os.path.join("images", "racecar.png"))
    # carImg = pygame.image.load(os.path.join(dir_name, "racecar.png"))
    pygame.display.set_icon(carImg)
except pygame.error:
    import traceback
    print(traceback.format_exc())
    carImg = None


def quit_the_game():
    pygame.quit()
    quit()


def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    mouse_is_pressed = pygame.mouse.get_pressed()[0]

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if mouse_is_pressed:
            action()

    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x+(w/2)), (y+(h/2)))
    gameDisplay.blit(textSurf, textRect)


def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodge: " + str(count), True, TEXT_COLOR)
    gameDisplay.blit(text, (0, 0))


def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])


def car(x, y):
    if carImg is None:
        pygame.draw.rect(gameDisplay, RED, (x + car_margin, y,
                                            car_width - 2 * car_margin,
                                            car_height))
    else:
        gameDisplay.blit(carImg, (x, y))


def text_objects(text, font):
    textSurface = font.render(text, True, TEXT_COLOR)
    return textSurface, textSurface.get_rect()


def crash():
    pygame.mixer.music.stop()
    crash_sound = pygame.mixer.Sound(CRASH_SOUND)
    pygame.mixer.Sound.play(crash_sound)

    # gameDisplay.fill(WHITE)
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects("You Crashed", largeText)
    TextRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    while True:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                quit_the_game()

        button("Play Again", display_width * 0.2,
               display_height * 0.8, BUTTON_WIDTH, BUTTON_HEIGHT,
               GREEN, bright_GREEN,
               action=game_loop)
        button("QUIT", display_width * 0.7, display_height *
               0.8, BUTTON_WIDTH, BUTTON_HEIGHT, RED, bright_RED, quit_the_game)

        pygame.display.update()
        clock.tick(15)


def unpause_the_game():
    pygame.mixer.music.unpause()
    global is_paused
    is_paused = False


def pause_the_game():
    pygame.mixer.music.pause()

    global is_paused
    is_paused = True

    # gameDisplay.fill(WHITE)
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects("Paused", largeText)
    TextRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    while is_paused:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                quit_the_game()
            if event.type == pygame.KEYDOWN:
                print 11, event.key
                if event.key in [pygame.K_p, pygame.K_ESCAPE]:
                    unpause_the_game()

        button("Continue", display_width * 0.2, display_height * 0.8,
               BUTTON_WIDTH, BUTTON_HEIGHT, GREEN, bright_GREEN,
               unpause_the_game)
        button("QUIT", display_width * 0.7, display_height * 0.8,
               BUTTON_WIDTH, BUTTON_HEIGHT, RED, bright_RED, quit_the_game)

        pygame.display.update()
        clock.tick(15)


def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                quit_the_game()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game_loop()

        gameDisplay.fill(BACKGROUD_COLOR)
        largeText = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects("A bit Racey", largeText)
        TextRect.center = ((display_width/2), (display_height/2))
        gameDisplay.blit(TextSurf, TextRect)
        button("PLAY", display_width * 0.2, display_height *
               0.8, BUTTON_WIDTH, BUTTON_HEIGHT, GREEN, bright_GREEN, game_loop)
        button("QUIT", display_width * 0.7, display_height *
               0.8, BUTTON_WIDTH, BUTTON_HEIGHT, RED, bright_RED, quit_the_game)

        pygame.display.update()
        clock.tick(15)


def reset_thing(thing_startx, thing_starty, thing_speed, dodged):
    if thing_starty > display_height:
        thing_starty = 0 - thing_height
        thing_startx = random.randrange(0, display_width)
        dodged += 1
        # car_speed += 60 / FPS
        thing_speed += float(THINGS_ACCELERATION) / FPS
    return thing_startx, thing_starty, thing_speed, dodged


def check_if_crashes(x, y, thing_speed, thing_startx, thing_starty):
    if y + thing_speed < thing_starty + thing_height and\
            y + car_height > thing_starty:
        if (x + car_margin > thing_startx and
                x + car_margin < thing_startx + thing_width) or (
                x + car_width - car_margin > thing_startx and
                x + car_width - car_margin < thing_startx + thing_width):
            crash()


def game_loop():
    try:
        pygame.mixer.music.load(MUSIC_GAME)
        pygame.mixer.music.play(-1)
    except pygame.error as ex:
        print ex

    x = (display_width * 0.45)
    y = (display_height * 0.75)

    x_change = 0
    car_speed = car_init_vel / FPS

    thing_startx = random.randrange(0, display_width)
    thing_starty = -display_height / 2
    thing2_startx = random.randrange(0, display_width)
    thing2_starty = -display_height
    thing_speed = thing_init_speed / FPS

    dodged = 0

    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_the_game()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = - car_speed
                elif event.key == pygame.K_RIGHT:
                    x_change = car_speed
                elif event.key in [pygame.K_p, pygame.K_ESCAPE]:
                    pause_the_game()
                # print event.key, x_change

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and x_change < 0:
                    x_change = 0
                if event.key == pygame.K_RIGHT and x_change > 0:
                    x_change = 0

        x += x_change

        gameDisplay.fill(BACKGROUD_COLOR)

        # things(thingx, thingy, thingw, thingh, color)
        things(thing_startx, thing_starty, thing_width, thing_height, THINGS_COLOR)
        things(thing2_startx, thing2_starty, thing_width, thing_height, THINGS_COLOR)
        thing_starty += thing_speed
        thing2_starty += thing_speed
        car(x, y)
        things_dodged(dodged)

        if x - car_margin > display_width - car_width or x + car_margin < 0:
            crash()

        thing_startx, thing_starty, thing_speed, dodged = \
            reset_thing(thing_startx, thing_starty, thing_speed, dodged)
        thing2_startx, thing2_starty, thing2_speed, dodged = \
            reset_thing(thing2_startx, thing2_starty, thing_speed, dodged)

        check_if_crashes(x, y, thing_speed, thing_startx, thing_starty)
        check_if_crashes(x, y, thing_speed, thing2_startx, thing2_starty)

        pygame.display.update()
        clock.tick(FPS)


game_intro()
game_loop()
quit_the_game()

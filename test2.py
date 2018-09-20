#!/usr/bin/env python


import os
import random
import pygame
pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

DISPLAY_WIDTH = 400
DISPLAY_HEIGHT = 300
DISPLAY_COLOR = BLACK
FPS = 5


# Player
WIDTH = 50
HEIGHT = 50
SPEED = 10
pipe_width = 10
pipe_gap = 10
pipe_speed = 5
between_pipe = 20

bird_group = pygame.sprite.Group()
pipe_group = pygame.sprite.Group()
game_folder = os.path.dirname(__file__)


class Bird(pygame.sprite.Sprite):
    def __init__(self, x_loc, y_loc, velocity):
        super(Bird, self).__init__()
        self.velocity = velocity
        self.x_loc = x_loc
        self.y_loc = y_loc
        # self.image = pygame.image.load(os.path.join(game_folder, "index2.png")).convert()

        img_name = "cactus.png"
        img_folder = os.path.join(game_folder, 'Platformer Art Complete Pack')
        img_folder = os.path.join(img_folder, 'Base pack')
        img_folder = os.path.join(img_folder, 'Items')
        img_path = os.path.join(img_folder, img_name)

        self.image = pygame.image.load(img_path).convert_alpha()
        self.image.set_colorkey(WHITE)
        self.image = pygame.transform.scale(self.image, (60, 65))
        self.rect = self.image.get_rect()
        self.rect.center = (x_loc, y_loc)

    def update(self):
        self.rect.y += self.velocity
        self.velocity = self.velocity+1
        self.mask = pygame.mask.from_surface(self.image)

    def jump(self):
        self.velocity = -10

    def boundary_collison(self):
        if self.rect.bottom+100 >= DISPLAY_HEIGHT or self.rect.top <= 0:
            return True


class UpperPipe(pygame.sprite.Sprite):
    """docstring for UpperPipe"""

    def __init__(self, pipe_x, pipe_height, pipe_speed):
        super(UpperPipe, self).__init__()
        self.pipe_speed = pipe_speed
        self.image = pygame.Surface((pipe_width, pipe_height))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = (pipe_x)
        self.rect.y = (0)

    def update(self):
        self.rect.x -= self.pipe_speed
        self.mask = pygame.mask.from_surface(self.image)

    def x_cord(self):
        return self.rect.x


class LowerPipe(pygame.sprite.Sprite):
    """docstring for UpperPipe"""

    def __init__(self, pipe_x, pipe_height, pipe_speed):
        super(LowerPipe, self).__init__()
        self.pipe_speed = pipe_speed
        self.image = pygame.Surface((pipe_width, DISPLAY_HEIGHT-(pipe_gap+pipe_height)))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = (pipe_x)
        self.rect.y = (pipe_height+pipe_gap)

    def update(self):
        self.rect.x -= self.pipe_speed
        self.mask = pygame.mask.from_surface(self.image)

    def x_cord(self):
        return self.rect.x


# class Cactus(pygame.sprite.Sprite):
#     def __init__(self):
#         pygame.sprite.Sprite.__init__(self)
#         # set up asset folders
#         img_name = "cactus.png"
#         img_folder = os.path.join(game_folder, 'Platformer Art Complete Pack')
#         img_folder = os.path.join(img_folder, 'Base pack')
#         img_folder = os.path.join(img_folder, 'Items')
#         img_path = os.path.join(img_folder, img_name)
#         self.image = pygame.image.load(img_path).convert_alpha()
#         self.image.set_colorkey(WHITE)
#         self.rect = self.image.get_rect()
#         self.rect.center = (DISPLAY_WIDTH / 2, DISPLAY_HEIGHT / 2)
#         self.mask = pygame.mask.from_surface(self.image)
#
#
# class Player(pygame.sprite.Sprite):
#     def __init__(self):
#         pygame.sprite.Sprite.__init__(self)
#         self.player_imgs = []
#         for i in range(1, 12):
#             print i
#             img_name = "p1_walk%s.png" % str(i if i > 9 else "0" + str(i))
#             print img_name
#             # set up asset folders
#             game_folder = os.path.dirname(__file__)
#             img_folder = os.path.join(game_folder, 'Platformer Art Complete Pack')
#             img_folder = os.path.join(img_folder, 'Base pack')
#             img_folder = os.path.join(img_folder, 'Player')
#             img_folder = os.path.join(img_folder, 'p1_walk')
#             img_folder = os.path.join(img_folder, 'PNG')
#             img_path = os.path.join(img_folder, img_name)
#             print "img_path", img_path, "..."
#             player_imgi = pygame.image.load(img_path).convert_alpha()
#             player_imgi.set_colorkey(BLACK)
#             self.player_imgs.append(player_imgi)
#         self.image = self.player_imgs[0]
#         self.image.set_colorkey(BLACK)
#         self.rect = self.image.get_rect()
#         self.rect.center = (0, DISPLAY_HEIGHT / 2)
#
#     def handle_events(self, event):
#         if event.type == pygame.KEYUP:
#             if event.key in [pygame.K_UP, pygame.K_SPACE]:
#                 self.rect.y += -20
#
#     def update(self):
#         self.image = self.player_imgs[(i * 11 / FPS) % 11]
#         self.rect.x += SPEED
#         if self.rect.left > DISPLAY_WIDTH:
#             self.rect.right = 0


screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
screen.fill(DISPLAY_COLOR)
clock = pygame.time.Clock()
# player_group = pygame.sprite.Group()
# cactus_group = pygame.sprite.Group()
# player = Player()
# cactus = Cactus()
# player_group.add(player)
# player_group.add(cactus)
x_loc, y_loc, velocity = 10, 10, 10
bird = Bird(x_loc, y_loc, velocity)
bird_group.add(bird)

pipe_list = []
init_pipe_x = 500
pipe_count = 10
for make in range(pipe_count):
    pipe_x = init_pipe_x+((between_pipe+pipe_width)*make)
    pipe_height = (round(random.uniform(0.2, 0.8), 2))*(DISPLAY_HEIGHT-pipe_gap)
    upper = UpperPipe(pipe_x, pipe_height, pipe_speed)
    lower = LowerPipe(pipe_x, pipe_height, pipe_speed)
    add_pipe = [upper, lower]
    pipe_list.append(add_pipe)
    pipe_group.add(upper)
    pipe_group.add(lower)


i = 0
while True:
    i += 1
    for event in pygame.event.get():
        # player.handle_events(event)
        if event.type == pygame.QUIT:
            print "quit"
            pygame.quit()
            quit(0)

    screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
    screen.fill(DISPLAY_COLOR)

    # player_group.draw(screen)
    # player_group.update()
    # cactus_group.draw(screen)
    # cactus_group.update()
    bird_hits = pygame.sprite.spritecollide(bird, pipe_group, False, pygame.sprite.collide_mask)
    if bird_hits:
        gameExit = True
    # print pygame.sprite.spritecollide(player_group, cactus_group, False, pygame.sprite.collide_mask)
    clock.tick(FPS)
    pygame.display.update()

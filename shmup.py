#!/usr/bin/env python
import pygame
import random
from os import path

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Game
GAME_NAME = "My Game"

# Screen
WIDTH = 360
HEIGHT = 480
FPS = 30


class Mob(pygame.sprite.Sprite):
    def __init__(self, game):
        pygame.sprite.Sprite.__init__(self)
        self.game = game

        self.image = pygame.Surface((30, 40))
        self.image.fill(RED)
        self.img_dir = path.join(self.game.img_png, "Meteors")
        self.img_path = path.join(self.img_dir, "meteorBrown_med1.png")
        self.img = pygame.image.load(self.img_path).convert()

        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedx = random.randrange(-2, 2)
        self.speedy = random.randrange(1, 8)

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.top > HEIGHT + 10 or self.rect.right < 0 or\
                self.rect.x > WIDTH:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedx = random.randrange(-2, 2)
            self.speedy = random.randrange(1, 8)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.game = game

        self.image = pygame.Surface((10, 20))
        self.image.fill(YELLOW)
        self.img_dir = path.join(self.game.img_png, "Lasers")
        self.img_path = path.join(self.img_dir, "laserRed16.png")
        self.bullet_img = pygame.image.load(self.img_path).convert()

        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        # kill if it moves off the top of the screen
        if self.rect.bottom < 0:
            self.kill()


class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        # self.image = pygame.Surface((50, 40))
        # self.image.fill(GREEN)
        self.img_path = path.join(self.game.img_png, "playerShip1_orange.png")
        self.image = pygame.image.load(self.img_path).convert()
        self.image.set_colorkey(BLACK)  # set borders to transparent color
        self.image = pygame.transform.scale(self.image, (50, 38))

        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0

    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -8
        if keystate[pygame.K_RIGHT]:
            self.speedx = 8
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self):
        bullet = Bullet(self.game, self.rect.centerx, self.rect.top)
        self.game.all_sprites.add(bullet)
        self.game.bullets.add(bullet)


class Game(object):
    def __init__(self):

        pygame.init()
        self.all_sprites = pygame.sprite.Group()
        # for sound
        pygame.mixer.init()

        # Load all game graphics
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(GAME_NAME)
        # background
        self.img_dir = path.join(path.dirname(__file__), 'SpaceShooterRedux')
        self.img_bg_dir = path.join(self.img_dir, 'Backgrounds')
        self.img_bg = path.join(self.img_bg_dir, 'starfield.png')
        self.img_png = path.join(self.img_dir, 'PNG')
        print self.img_bg
        self.background = pygame.image.load(self.img_bg).convert()
        self.background_rect = self.background.get_rect()
        self.draw_graphics()

        clock = pygame.time.Clock()

        player = Player(self)
        self.all_sprites.add(player)
        self.bullets = pygame.sprite.Group()
        self.mobs = pygame.sprite.Group()
        for i in range(8):
            m = Mob(self)
            self.all_sprites.add(m)
            self.mobs.add(m)

        self.cmd_key_down = False
        # Game loop
        self.running = True
        while self.running:
            clock.tick(FPS)
            # Process input (events)
            for event in pygame.event.get():
                self.handle_common_events(event)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        player.shoot()
            # Update
            self.all_sprites.update()
            hits = pygame.sprite.spritecollide(player, self.mobs, False)
            if hits:
                self.running = False
            # check to see if a bullet hit a mob
            hits = pygame.sprite.groupcollide(self.bullets, self.mobs,
                                              True, True)
            for hit in hits:
                m = Mob(self)
                self.all_sprites.add(m)
                self.mobs.add(m)
            # Render (draw)
            self.draw_graphics()

            pygame.display.flip()

        pygame.quit()

    def handle_common_events(self, event):
        # check for closing window
        if event.type == pygame.QUIT:
            self.quit()

        if event.type == pygame.KEYDOWN:
            if event.key == 310:
                self.cmd_key_down = True
            if self.cmd_key_down and event.key == pygame.K_q:
                self.quit()

        if event.type == pygame.KEYUP:
            if event.key == 310:
                self.cmd_key_down = False

    def draw_graphics(self):
        self.screen.fill(BLACK)
        self.screen.blit(self.background, self.background_rect)
        self.all_sprites.draw(self.screen)

    def quit(self):
        self.running = False


Game()

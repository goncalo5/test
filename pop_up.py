#!/usr/bin/env python
from os import path
import random
import pygame as pg

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
DARKBLUE = (0, 0, 100)
YELLOW = (255, 255, 0)

# Screen
DISPLAY = {
    'title': "My Game",
    'tilesize': 32,
    'width': 360,
    'height': 480,
    'bgcolor': DARKBLUE,
    'fps': 60
}

# PopUp
POP_UP = {
    'layer': 2,
    'pos': (50, 100),
    'size': (250, 150),
    'color': YELLOW
}


# class Button(object):
class Button(pg.sprite.Sprite):
    def __init__(self, game, **kwargs):
        # self._layer = -1
        # self.groups = game.all_sprites
        super(Button, self).__init__()
        # super(Button, self).__init__(self.groups)
        self.game = game
        self.kwargs = kwargs
        self.size = kwargs.get('size')
        self.pos = kwargs.get('pos')
        self.color = kwargs.get('color')

        self.image = pg.Surface(self.size)
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        #
        self.surface = kwargs.get('surface')

        self.rect.topleft = self.pos
        self.surface[0].blit(self.image, self.rect)

        self.rect.x = self.pos[0] + self.surface[1].x
        self.rect.y = self.pos[1] + self.surface[1].y

    # def update(self):
    #     print('update button')
    #     self.surface.blit(self.image, self.rect)


class PopUp(pg.sprite.Sprite):
    def __init__(self, game):
        self._layer = POP_UP['layer']
        self.groups = game.all_sprites
        super(PopUp, self).__init__(self.groups)
        self.game = game
        self.image = pg.Surface(POP_UP['size'])
        self.image.fill(POP_UP['color'])
        self.rect = self.image.get_rect()
        self.rect.topleft = POP_UP['pos']
        self.dx = 0
        self.dy = 0
        self.bar_down = 0

        self.buttons = {}
        # print('create button close')
        self.buttons['bar'] = Button(game, surface=(self.image, self.rect),
                                     pos=(0, 0), size=(self.rect.width, 20), color=GREEN)
        # print('create button close')
        self.buttons['close'] = Button(game, surface=(self.image, self.rect),
                                       pos=(2, 2), size=(15, 15), color=RED)
        # print('create button ok')
        self.buttons['ok'] = Button(game, surface=(self.image, self.rect),
                                    pos=(100, 100), size=(30, 30), color=WHITE)

    def update(self):
        rel = pg.mouse.get_rel()
        pressed = pg.mouse.get_pressed()

        # print('dx', self.dx, 'dy', self.dy, rel)
        self.rect.x += self.dx
        self.rect.y += self.dy
        for button in self.buttons.values():
            button.rect.x += self.dx
            button.rect.y += self.dy
        self.dx = 0
        self.dy = 0
        if pressed == (1, 0, 0):
            print('pressed')
            if self.buttons['bar'].rect.collidepoint(pg.mouse.get_pos()):
                print('bar', rel)
                self.bar_down = 1
            if self.bar_down:
                self.dx = rel[0]
                self.dy = rel[1]
            if self.buttons['ok'].rect.collidepoint(pg.mouse.get_pos()):
                print('ok')
            if self.buttons['close'].rect.collidepoint(pg.mouse.get_pos()):
                print(self.buttons['close'].rect.collidepoint(
                    pg.mouse.get_pos()), rel)
                for button in self.buttons.values():
                    button.kill()
                self.kill()
        if pressed == (0, 0, 0):
            self.bar_down = 0


class Game(object):
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((DISPLAY['width'], DISPLAY['height']))
        pg.display.set_caption(DISPLAY['title'])
        self.clock = pg.time.Clock()

        # variables
        self.cmd_key_down = False

        self.load_data()
        self.new()
        self.run()

        pg.quit()

    def load_data(self):
        self.dir = path.dirname(__file__)
        pg.mixer.init()  # for sound

    def new(self):
        # start a new game
        self.all_sprites = pg.sprite.LayeredUpdates()
        self.player = PopUp(self)

    def run(self):
        # game loop - set  self.playing = False to end the game
        self.running = True
        while self.running:
            self.clock.tick(DISPLAY['fps'])
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pg.event.get():
            self.handle_common_events(event)

    def handle_common_events(self, event):
        # check for closing window
        if event.type == pg.QUIT:
            # force quit
            quit()

        if event.type == pg.KEYDOWN:
            if event.key == 310:
                self.cmd_key_down = True
            if self.cmd_key_down and event.key == pg.K_q:
                # force quit
                quit()

        if event.type == pg.KEYUP:
            if event.key == 310:
                self.cmd_key_down = False

    def update(self):
        # update portion of the game loop
        self.all_sprites.update()

    def draw(self):
        pg.display.set_caption('%s - fps: %.5s' %
                               (DISPLAY['title'], self.clock.get_fps()))
        self.screen.fill(DISPLAY['bgcolor'])
        self.all_sprites.draw(self.screen)

        pg.display.flip()

    def quit(self):
        self.running = False


Game()

#!/usr/bin/env python
from os import path
import random
import pygame as pg

BLACK = (0, 0, 0)
GREY = (128, 128, 128)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
DARKGREEN = (0, 155, 0)
BLUE = (0, 0, 255)
DARKBLUE = (0, 0, 100)
LIGHTBLUE = (200, 200, 255)
YELLOW = (255, 255, 0)

# resources
resources = {"food": 200, "wood": 0, "stone": 0, "metal": 0}

# units
units = {
    "villager": {
        "name": "Villager",
        "shortname": "v",
        "n": 0,
        "cost": {
            "food": 50,
        },
        "attack": 1,
        "life": 15,
    },
    "spearman": {
        "name": "Spearman",
        "shortname": "sp",
        "n": 0,
        "cost": {
            "food": 50,
            "wood": 10,
            "metal": 8,
        },
        "attack": 7,
        "life": 30,
    },
    "axeman": {
        "name": "Axeman",
        "n": 0,
        "cost": {
            "food": 50,
            "metal": 15,
        },
        "attack": 10,
        "life": 25,
    },
    "swordsman": {
        "name": "Swordsman",
        "n": 0,
        "cost": {
            "food": 50,
            "wood": 5,
            "metal": 25,
        },
        "attack": 12,
        "life": 50,
    },
    "cavalry": {
        "name": "Cavalry",
        "n": 0,
        "cost": {
            "food": 200,
            "wood": 15,
            "metal": 25,
        },
        "attack": 15,
        "life": 80
    }
}

# Screen
DISPLAY = {
    'title': "RPG Game",
    'tilesize': 32,
    'width': 600,
    'height': 600,
    'bgcolor': DARKBLUE,
    'fps': 30
}

# menus
MENU = {
    'color': LIGHTBLUE
}
MAIN_MENU = {
    'buttons': ['recruit_menu'],
    'color': LIGHTBLUE,
    "content": {
        "text": "Main Menu",
        "color": WHITE,
        "size": 30,
        "pos": (100, 50),
    }
}
RECRUIT_MENU = {
    'buttons': ['menu'],
    'color': LIGHTBLUE,

}
RESOURCES_LABEL = {
    "title": {
        "text": "Resources:",
        "color": DARKGREEN,
        "size": 30,
        "pos": (20, 50),
        "pos_rel": "topleft",
    },
    "content": {
        "color": BLACK,
        "size": 25,
        "pos": (150, 50),
        "pos_rel": "topleft",
    }
}
UNITS_LABEL = {
    "title": {
        "text": "Units",
        "color": BLUE,
        "size": 30,
        "pos": (20, 150),
        "pos_rel": "topleft",
    },
    "content": {
        "color": BLACK,
        "size": 25,
        "pos": (20, 180),
        "pos_rel": "topleft",
    }
}

# buttons
BUTTONS = {
    'menu': {
        'id': 'menu',
        'size': {
            'normal': (150, 75),
            'hovered': (160, 80),
        },
        'pos': ('right', DISPLAY['height'] - 50),
        'color': {
            'normal': BLACK,
            'hovered': GREY
        },
        'text': {
            'content': 'Menu',
            'size': 40,
            'color': YELLOW,
        },
    },
    'recruit_menu': {
        'id': 'recruit_menu',
        'size': {
            'normal': (150, 75),
            'hovered': (160, 80),
        },
        'pos': (100, 300),
        'color': {
            'normal': BLACK,
            'hovered': GREY
        },
        'text': {
            'content': 'Recruit',
            'size': 35,
            'color': YELLOW,
        },
    },
}


def draw_text(screen, text="test", size=25, color=BLACK,
              pos=(0, 0), pos_rel="midtop", font='arial'):
    try:
        font = pg.font.Font(font, size)
    except IOError:
        font = pg.font.SysFont(font, size)
    text_surface = font.render(str(text), False, color)
    text_rect = text_surface.get_rect()
    setattr(text_rect, pos_rel, pos)
    screen.blit(text_surface, text_rect)


class Button(pg.sprite.Sprite):
    def __init__(self, game, **kwargs):
        self.groups = game.all_sprites, game.buttons
        super(Button, self).__init__(self.groups)
        self.game = game
        self.kwargs = kwargs
        self.id = kwargs.get('id')
        print('create button', self.id)

        print(kwargs)
        # size:
        self.size = kwargs.get('size', {}).get('normal', (150, 75))
        self.size_hovered = kwargs.get('size', {}).get('hovered', self.size)

        # pos:
        screen_w, screen_h = self.game.screen.get_size()
        self.pos = list(kwargs.get('pos'))
        if self.pos[0] == 'right':
            self.pos[0] = screen_w - self.size[0]

        # color:
        self.color = kwargs.get('color', {}).get('normal', BLACK)
        self.color_hovered = kwargs.get('color', {}).get('hovered', self.color)

        # images:
        self.image_normal = pg.Surface(self.size)
        self.image_normal.fill(self.color)
        self.rect_normal = self.image_normal.get_rect()
        self.image = self.image_normal
        self.rect = self.rect_normal

        self.image_hovered = pg.Surface(self.size_hovered)
        self.image_hovered.fill(self.color_hovered)
        self.rect_hovered = self.image_hovered.get_rect()
        self.hovered = 0

        # text:

        self.text = kwargs.get('text_content',
                               kwargs.get('text').get('content'))
        self.text_size = self.kwargs.get('text', {}).get('size', 30)
        self.text_color = self.kwargs.get('text', {}).get('color', WHITE)
        self.text_pos = (self.size[0] / 2, 10)
        print(self.text, self.text_size, self.text_color)

        self.time_to_unpress = pg.time.get_ticks()

    def events(self):

        if pg.time.get_ticks() - self.time_to_unpress < 300:
            return

        if not self.rect.collidepoint(pg.mouse.get_pos()):
            return

        if pg.mouse.get_pressed() == (1, 0, 0):

            self.time_to_unpress = pg.time.get_ticks()
            print('button', self.id)
            if self.id == 'menu':
                self.game.change_menu('MainMenu')
            if self.id == 'recruit_menu':
                self.game.change_menu('RecruitMenu')

    def update(self):
        if pg.mouse.get_rel():
            self.hovered = self.rect.collidepoint(pg.mouse.get_pos())

        if self.hovered:
            self.image = self.image_hovered
            self.rect = self.rect_hovered
        else:
            self.image = self.image_normal
            self.rect = self.rect_normal
        self.rect.center = self.pos

        draw_text(self.image, self.text, self.text_size,
                  self.text_color, self.text_pos)

        self.events()


class Menu(pg.sprite.Sprite):
    def __init__(self, game):
        self.groups = game.all_sprites
        super(Menu, self).__init__(self.groups)
        self.game = game
        self.image = pg.Surface(self.game.screen.get_size())
        self.image.fill(self.settings['color'])
        self.rect = self.image.get_rect()

        for button_name in self.settings['buttons']:
            Button(self.game, **BUTTONS[button_name])

    def create_resources_label(self):
        draw_text(self.image, **RESOURCES_LABEL["title"])
        draw_text(self.image, text=resources, **RESOURCES_LABEL["content"])

    def create_units_label(self):
        draw_text(self.image, **UNITS_LABEL["title"])
        text = "   ".join("{}: {}".format(value["name"], value["n"]) for value in units.values())
        draw_text(self.image, text=text, **UNITS_LABEL["content"])


class MainMenu(Menu):
    def __init__(self, game):
        self.settings = MAIN_MENU
        super(MainMenu, self).__init__(game)

    def update(self):
        self.create_resources_label()
        self.create_units_label()


class RecruitMenu(Menu):
    def __init__(self, game):
        self.settings = RECRUIT_MENU
        super(RecruitMenu, self).__init__(game)
        self.name = 'recruit_menu'

    def update(self):
        # self.image.fill(RECRUIT_MENU['color'])
        self.create_resources_label()
        self.create_units_label()


class Game(object):
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((DISPLAY['width'], DISPLAY['height']))
        pg.display.set_caption(DISPLAY['title'])
        self.clock = pg.time.Clock()

        # units:
        draw_text(self.screen, **UNITS_LABEL["title"])
        text = "   ".join("{}: {}".format(value["name"], value["n"]) for value in units.values())
        draw_text(self.screen, text=text, **UNITS_LABEL["content"])

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
        self.all_sprites = pg.sprite.LayeredUpdates()
        self.buttons = pg.sprite.Group()
        MainMenu(self)

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
        # self.screen.fill(DISPLAY['bgcolor'])
        self.all_sprites.draw(self.screen)

        # draw_text(self.screen, "test", 12, GREEN, (100, 100))

        pg.display.flip()

    def clear_all_sprites(self):
        for sprite in self.all_sprites:
            sprite.kill()

    def change_menu(self, new_menu):
        self.clear_all_sprites()
        exec('%s(self)' % new_menu)

    def quit(self):
        self.running = False


Game()

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.graphics import *

from kivy.event import EventDispatcher
from kivy import properties as kp

FPS = 60

CONVERT_CODE2KEY = {
    82: "up",
    79: "right",
    81: "down",
    80: "left",
    44: "spacebar"
}

WIDTH = 600
HEIGHT = 500

# Player properties
PLAYER_X = 0.7
PLAYER_Y = 0.2
PLAYER_WIDTH = 0.12
PLAYER_HEIGHT = 0.12
PLAYER_ACC = 1000
PLAYER_FRICTION = -5
PLAYER_STOP_ANIM_WITH_VEL = 25
# PLAYER_GRAV = -500
PLAYER_JUMP = .5
PLAYER_TIME_IN_JUMP = .4
PLAYER_ANIMATION_WALK = 0.2
PLAYER_ANIMATION_IDLE = 0.35


class Player(Widget):
    vel = kp.ObjectProperty(Vector(0, 0))
    acc = kp.ObjectProperty(Vector(0, 0))
    max_h = kp.NumericProperty(0)
    total_time = kp.NumericProperty(0)
    gravity = kp.NumericProperty(-2*PLAYER_JUMP*Window.height/PLAYER_TIME_IN_JUMP**2)

    def __init__(self, game, **kwargs):
        super().__init__(**kwargs)
        self.game = game


    def update(self, dt):
        # print("update")
        # print("y", self.y)
        # print("vel", self.vel.y)
        # print("acc", self.acc.y)
        # print(self.pos)
        # print("time", self.total_time)
        self.total_time += dt
        if self.y == 0:
            # print(self.total_time)
            acc_y = 0
            self.vel.y = 0
        else:
            acc_y = self.gravity
            # acc_y = PLAYER_GRAV
        self.acc = Vector(0, acc_y)
        if "left" in self.game.keys:
            self.x -= 2
        if "right" in self.game.keys:
            self.x += 2
        if "spacebar" in self.game.keys:
            print("jump")
            self.jump(dt)
        # eq of motion
        self.vel += self.acc * dt
        self.pos = Vector(self.pos) + self.vel * dt + 0.5 * self.acc * dt**2

        self.max_h = max(self.y, self.max_h)

        if self.y < 0:
            self.y = 0


    def jump(self, dt):
        if self.y == 0:
            print("vel", self.vel.y)
            print("max_h", self.max_h, self.max_h / Window.height, Window.height)
            y = PLAYER_JUMP * Window.height
            print("y", y)
            # self.vel.y += PLAYER_JUMP * Window.height
            # self.vel.y = PLAYER_JUMP * Window.height / 1 + 0.5 * PLAYER_GRAV * 1
            self.vel.y = 2 * y / PLAYER_TIME_IN_JUMP
            self.max_h = 0
            print("new vel", self.vel.y)
            # self.acc = Vector(0, -PLAYER_GRAV)


class Cloud(Widget):
    pass


class Cloud2(Widget):
    pass


class Game(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.keys = set()
        Window.bind(on_key_down=self._on_keyboard_down)
        Window.bind(on_key_up=self._on_keyboard_up)
        Clock.schedule_interval(self.update, 1.0/FPS)
        self.player = Player(self)
        self.add_widget(self.player, index=3)  # white
        self.add_widget(Cloud(), index=2)  # red
        self.add_widget(Cloud2(), index=1)  # green
    
    def update(self, dt):
        self.player.update(dt)
        


    def _on_keyboard_up(self, *args):
        keycode = args[2]
        try:
            key = CONVERT_CODE2KEY[keycode]
        except KeyError:
            return
        try:
            self.keys.remove(key)
        except:
            pass
    
    def _on_keyboard_down(self, *args):
        keycode = args[2]
        try:
            key = CONVERT_CODE2KEY[keycode]
        except KeyError:
            return
        self.keys.add(key)


class TestApp(App):
    def build(self):
        Window.size = (WIDTH, HEIGHT)
        self.game = Game()
        return self.game

if __name__ == "__main__":
    TestApp().run()

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty, BooleanProperty, StringProperty
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.vector import Vector


FPS = 10
# x:
FRICTION = .4
SPEED = 100
MAX_ACC = 350
# y:
GRAVITY = 5000
JUMP = 3500


class Platform(Widget):
    pass


class Player(Widget):
    dist = ObjectProperty(Vector(0, 0))
    vel = ObjectProperty(Vector(0, 0))
    acc = ObjectProperty(Vector(0, 0))

    touch_the_ground = BooleanProperty(False)
    touch_the_platform = BooleanProperty(False)


class Game(Widget):
    player = ObjectProperty(None)
    platform = ObjectProperty(None)

    def __init__(self):
        super().__init__()
        self._keyboard = Window.request_keyboard(
            None, self, 'text')
        self._keyboard.bind(on_key_down=self._on_keyboard_down)
        self._keyboard.bind(on_key_up=self._on_keyboard_up)

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        # print("down", keyboard, keycode)
        if keycode[1] == "right":
            if self.player.touch_the_ground or self.player.touch_the_platform:
                if self.player.acc.x > -MAX_ACC:
                    self.player.vel.x += SPEED

        if keycode[1] == "left":
            if self.player.touch_the_ground or self.player.touch_the_platform:
                if self.player.acc.x < MAX_ACC:
                    self.player.vel.x -= SPEED

        if keycode[1] == "spacebar":
            if self.player.touch_the_ground or self.player.touch_the_platform:
                print("\nJUMP")
                self.player.dist.y += 10
                self.player.vel.y += JUMP
                self.player.pos = self.player.dist
                self.player.touch_the_ground = False
                self.player.touch_the_platform = False


    def _on_keyboard_up(self, keyboard, keycode):
        print("up", keyboard, keycode)

    def update(self, dt):
        # print("update")
        print(self.player.dist, self.player.vel, self.player.acc, self.player.touch_the_ground, self.player.touch_the_platform)


        # check the ground:
        if self.player.dist.y < 10:
            self.player.touch_the_ground = True
        else:
            self.player.touch_the_ground = False
        if self.player.touch_the_ground or self.player.touch_the_platform:
            self.player.acc.y = 0
            self.player.vel.y = 0
        else:
            self.player.acc.y = -GRAVITY
        print(1, self.player.dist, self.player.vel, self.player.acc, self.player.touch_the_ground, self.player.touch_the_platform)
        
        # Friction:
        if self.player.touch_the_ground or self.player.touch_the_platform:
            self.player.acc.x = -FRICTION * self.player.vel.x
        else:
            print("no friction")
            self.player.acc.x = 0
        print(2, self.player.dist, self.player.vel, self.player.acc, self.player.touch_the_ground, self.player.touch_the_platform)

        # kinematic equations:
        self.player.vel +=  self.player.acc * dt
        self.player.dist += self.player.vel * dt + self.player.acc * dt ** 2 / 2.
        print(3, self.player.dist, self.player.vel, self.player.acc, self.player.touch_the_ground, self.player.touch_the_platform)
    
        # small ajusts:
        if abs(self.player.vel.x) < 5:
            self.player.vel.x = 0
        if self.player.dist.y < 0:
            self.player.dist.y = 0
        print(4, self.player.dist, self.player.vel, self.player.acc, self.player.touch_the_ground, self.player.touch_the_platform)


        self.player.pos = self.player.dist

        # collisions:
        if self.player.collide_widget(self.platform):
            print("colide", self.player.vel.y < 0 and self.player.y > self.platform.top, self.player.vel.y < 0, self.player.y > self.platform.top)
            # print(self.player.collide_widget(self.platform))
            # self.player.x = self.platform.top
            if self.player.vel.y < 0:# and self.player.y > self.platform.top:
                self.player.dist.y = self.platform.top
                self.player.vel.y = 0
                self.player.acc.y = 0
                self.player.touch_the_platform = True
                self.player.pos = self.player.dist
        else:
            self.player.touch_the_platform = False


class PlatformsApp(App):
    window = ObjectProperty(Window)
    
    def build(self):
        # print(self.window.size)
        self.window.clearcolor = (0.2, 0.2, 0.2, 1)
        game = Game()
        Clock.schedule_interval(game.update, 1.0/FPS)
        return game


if __name__ == '__main__':
    PlatformsApp().run()
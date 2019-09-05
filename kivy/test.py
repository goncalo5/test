# Joystick / Gamepad example
# STOP_FIRE from https://wiki.libsdl.org/SDL_JoyAxisEvent

from kivy.app import App
from kivy.clock import Clock
from kivy.uix.widget import Widget
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy import properties as kp
from kivy.vector import Vector


class Joystick(RelativeLayout):
    sticky = kp.BooleanProperty(False)  # When False, the joystick will snap back to center on_touch_up.

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.max_dist = self.width / 2
        # print(self.max_dist)
        self.magnitude = 0

    def on_touch_down(self, *args):
        # print("on_touch_down", args)
        touch = args[0]
        print(touch.pos)
        self.stick.center = touch.pos


    def on_touch_move(self, *args):
        # print("on_touch_down", args)
        touch = args[0]
        print(touch.pos, self.center)
        self.stick.center = touch.pos

        vec_touch = Vector(*touch.pos)
        vec_center = Vector(*self.center)
        vec_diff = vec_touch - vec_center

        # dist = vec_touch.distance(vec_center)
        dist = vec_diff.length()
        angle = -Vector(1, 0).angle(vec_diff)

        if dist > self.max_dist:
            dist = self.max_dist
            vec_diff = vec_diff.normalize() * self.max_dist
            vec_touch = vec_diff + vec_center
            self.stick.center = vec_touch
        self.magnitude = dist / self.max_dist

        print("magnitude: %s, angle: %s" % (self.magnitude, angle))


class Game(Screen):
# class Game(Screen):
    pass

class TestApp(App):
    width = kp.NumericProperty(Window.width)
    height = kp.NumericProperty(Window.height)
    def build(self):
        print(Window.size)
        return Game()


if __name__ == '__main__':
    TestApp().run()
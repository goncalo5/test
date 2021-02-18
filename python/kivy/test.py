# kivy:
from kivy.app import App
from kivy.clock import Clock
from kivy import properties as kp
from kivy.core.window import Window
from kivy.event import EventDispatcher
# uix:
from kivy.uix.widget import Widget
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.screenmanager import ScreenManager, Screen


class Selected(EventDispatcher):
    n = kp.NumericProperty(0)

class Player(EventDispatcher):
    selected = kp.ObjectProperty(Selected())

class Game(Screen):
    player = kp.ObjectProperty(Player())


class TestApp(App):
    game = kp.ObjectProperty(Game())
    def build(self):
        self.game = Game()
        return self.game


if __name__ == '__main__':
    TestApp().run()
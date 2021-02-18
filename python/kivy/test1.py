from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.image import Image
from random import *
from kivy.clock import Clock


class Sprite(Image):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def add_to_groups(self, index):
        self.game.add_widget(self, index=index)


class Player(Sprite):
    def __init__(self, game, **kwargs):
        super().__init__(source="imgs/bunny1_stand.png")
        self.game = game
        self.add_to_groups(index=0)

    def on_touch_move(self, touch):
        self.center = touch.pos

class Cloud(Sprite):
    def __init__(self, game, **kwargs):
        super().__init__(**kwargs)
        self.source = "imgs/cloud%s.png" % randrange(1, 4)
        self.x = uniform(0, Window.width)
        self.y = uniform(0, Window.height)
        self.game = game
        self.add_to_groups(index=1)

class Blue(Sprite):
    pass


class MainWidget(Widget):
    pass
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


        Player(self)

        # for i in range(10):
        #     Cloud(game=self)
        self.add_widget(Blue(), index=2)
        Clock.schedule_interval(self.update, .1)
    
    def update(self, dt):
        Cloud(self)


class Test2App(App):
    def build(self):
        Window.size = (300, 300)
        self.main_widget = MainWidget()
        return self.main_widget

if __name__ == "__main__":
    Test2App().run()
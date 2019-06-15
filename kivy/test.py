from kivy.config import Config
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
import kivy
kivy.require("1.9.0")
 
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy import properties as kp
from kivy.animation import Animation
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.graphics import Rotate, Rectangle


class Sprite(Image): 
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size = self.texture_size

class Player(Sprite):
    def __init__(self, **kwargs):
        super().__init__(source="imgs/BirdS_0000_Capa-1.png")
        # self.source="imgs/BirdS_0000_Capa-1.png"
        with self.canvas.before:
            Rotate(axis=(0,1,0), angle=180, origin=self.center)
            # Rectangle(pos=self.pos, size=self.size, source="imgs/BirdS_0000_Capa-1.png")


class Test(Widget):
    pass


class TestApp(App):

    def build(self):
        print("build")
        Window.bind(on_keyboard=self.key_handler)

        return Test()
    
    def key_handler(self, *args):
        print(args)
 
TestApp().run()
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

class Player(Widget):
    pass

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
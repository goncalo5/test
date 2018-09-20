#!/usr/bin/env python

from kivy.app import App
# from kivy.uix.label import Label
from kivy.uix.widget import Widget
# from kivy.uix.textinput import TextInput
# from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Line
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import Screen
from kivy.uix.screenmanager import FadeTransition


class ClearWidget(Widget):

    def on_touch_down(self, touch):
        with self.canvas:
            touch.ud["line"] = {}


class Painter(Widget):
    # id = "draw"

    def on_touch_down(self, touch):

        with self.canvas:
            touch.ud["line"] = Line(points=[touch.x, touch.y])

    def on_touch_move(self, touch):
        try:
            touch.ud["line"].points += [touch.x, touch.y]
        except KeyError as e:
            print e
        print touch.ud


class MainScreen(Screen):
    pass


class AnotherScreen(Screen):

    def clear_screen(self, draw):
        print "clear_screen", self, draw
        print dir(self)
        print dir(draw)
        print draw.__dict__
        self.remove_widget(draw)
        # try:
        #     self.remove_widget(self.draw)
        # except:
        #     pass
        draw = Painter()
        self.add_widget(draw)


class ScreenManagement(ScreenManager):
    pass


presentation = Builder.load_file("test.kv")


class MainApp(App):
    def build(self):
        return presentation


MainApp().run()

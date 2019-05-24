from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse, Line
from kivy.core.window import Window
from kivy.uix.button import Button
from random import random
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.clock import Clock


class Resources(GridLayout):
    food = NumericProperty(200)

    def update(self):
        print("update resources")
        self.food += 1

class MyRootWidget(GridLayout):
    resources = ObjectProperty(None)
    def do_something(self):
        print(11)


    def update(self, dt):
        pass
        # print("update resources")
        # self.resources.food += 1
        self.resources.update()

class TestApp(App):


    # python:
    # def build(self):
    #     root = MyRootWidget()
    #     box = BoxLayout()
    #     box.add_widget(Button())
    #     box.add_widget(Button())
    #     root.add_widget(box)
    #     return root

    # .kv:
    def build(self):
        root = MyRootWidget()

        Clock.schedule_interval(root.update, 1.0/60.0)
        return root



if __name__ == '__main__':
    TestApp().run()
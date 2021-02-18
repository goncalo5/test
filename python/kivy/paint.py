from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse, Line
from kivy.core.window import Window
from kivy.uix.button import Button
from random import random


class MyPaintWidget(Widget):

    def __init__(self):
        super(MyPaintWidget, self).__init__()

        Window.bind(mouse_pos=self.mouse_pos)

    def on_touch_down(self, touch):
        color = (random(), random(), random())
        with self.canvas:
            Color(*color)
            d = 30.
            Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
            touch.ud['line'] = Line(points=(touch.x, touch.y))

    def mouse_pos(self, window, pos):
        # print(window.__dict__)
        print(str(pos))

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]

    # def on_touch_up(self, touch):
    #     print("on_touch_up", touch, [touch.x, touch.y], touch.ud)
    #     touch.ud['line'].points += [touch.x, touch.y]


class MyPaintApp(App):
    def update(self):
        pass

    def build(self):
        parent = Widget()
        self.painter = MyPaintWidget()
        clearbtn = Button(text='Clear')
        clearbtn.bind(on_release=self.clear_canvas)
        parent.add_widget(self.painter)
        parent.add_widget(clearbtn)
        return parent

    def clear_canvas(self, obj):
        self.painter.canvas.clear()


if __name__ == '__main__':
    MyPaintApp().run()
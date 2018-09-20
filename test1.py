import inspect
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import Screen
from kivy.uix.screenmanager import FadeTransition
from kivy.graphics import Line

# Builder.load_string(
#     '''
# <SmallButton@Button>:
#     font_size: 20
#     size_hint: 0.2, 0.15
#
# <BigButton@Button>:
#     font_size: 40
#     size_hint: 0.4, 0.3
#
# <FloatLayout>:
#     SmallButton:
#         pos_hint: {"x":0, "top": 1}
#     BigButton:
#     Slider:
#
# ''')

for x in dir(ScreenManager):
    print x


class Painter(Widget):
    def on_touch_down(self, touch):
        with self.canvas:
            touch.ud["line"] = Line(points=[touch.x, touch.y])

    def on_touch_move(self, touch):
        try:
            touch.ud["line"].points += [touch.x, touch.y]
        except KeyError as e:
            print e
        print touch.ud


class MyApp(App):
    def build(self):
        self.sm = ScreenManager(transition=FadeTransition())

        # screen1
        self.screen1 = Screen(name="screen1")

        self.hello = Label(text="Hello")
        self.screen1.add_widget(self.hello)

        self.small_button = Button(
            text="Clear",
            size_hint=(0.2, 0.15),
            pos_hint={"x": 0, "top": 1})
        self.small_button.bind(on_press=self.clear_screen)
        self.screen1.add_widget(self.small_button)

        self.small_button_change = Button(
            text="Change",
            size_hint=(0.2, 0.15),
            pos_hint={"right": 1, "y": 0})
        self.small_button_change.bind(on_press=self.change_screen)
        self.screen1.add_widget(self.small_button_change)

        self.sm.add_widget(self.screen1)

        # screen2
        self.screen2 = Screen(name="screen2")
        self.small_button_change_back = Button(
            text="Change",
            size_hint=(0.2, 0.15),
            pos_hint={"right": 1, "y": 0})
        self.small_button_change_back.bind(on_press=self.change_screen_back)
        self.screen2.add_widget(self.small_button_change_back)

        self.small_button_clear_draw = Button(
            text="Clear",
            size_hint=(0.2, 0.15),
            pos_hint={"x": 0, "top": 1})
        self.small_button_clear_draw.bind(on_press=self.clear_screen2)
        self.screen2.add_widget(self.small_button_clear_draw)

        self.draw = Painter()
        self.screen2.add_widget(self.draw)

        self.sm.add_widget(self.screen2)

        return self.sm

    def clear_screen(self, instance):
        print "clear_screen", instance
        self.screen1.remove_widget(self.hello)

    def clear_screen2(self, instance):
        print "clear_screen", instance
        self.screen2.remove_widget(self.draw)

    def change_screen(self, instance):
        print "change_screen", instance
        self.root.current = "screen2"

    def change_screen_back(self, instance):
        print "change_screen_back", instance
        self.root.current = "screen1"

    def quit_app(self, instance):
        print "quit_app", instance
        self.stop()


MyApp().run()

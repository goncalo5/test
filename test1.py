from kivy.app import App
from kivy.uix.button import Button
from kivy.event import EventDispatcher
from kivy import properties as kp


class Addition(EventDispatcher):
    xp = kp.NumericProperty(0)

class TestApp(App):
    addition = kp.ObjectProperty(Addition())
    def build(self):

        return Button(
            text=str(self.addition.xp),
            on_press=self.change_button()
        )
    def change_button(self):
        self.addition.xp += 1

if __name__ == "__main__":
    TestApp().run()

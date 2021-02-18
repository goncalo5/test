
from kivy.app import App
from kivy.uix.button import Button

class GameApp(App):
    def build(self):
        return Button(text="ok")

if __name__ == "__main__":
    GameApp().run()
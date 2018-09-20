import kivy
kivy.require("1.9.0")

from kivy.app import App
from kivy.uix.gridlayout import GridLayout


class SampGridLayout(GridLayout):
    pass


class ToolbarApp(App):

    def build(self):
        return SampGridLayout()


sample_app = ToolbarApp()
sample_app.run()

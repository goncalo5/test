from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.uix.label import Label
from kivy.uix.button import Button

from kivy.clock import Clock

FPS = 1

# resources
RESOURCES = {"food": 200, "wood": 0, "stone": 0, "metal": 0}

# units
UNITS = {
    "villager": {
        "name": "Villager",
        "shortname": "v",
        "n": 0,
        "cost": {
            "food": 50,
        },
        "attack": 1,
        "life": 15,
    },
    "spearman": {
        "name": "Spearman",
        "shortname": "sp",
        "n": 0,
        "cost": {
            "food": 50,
            "wood": 10,
            "metal": 8,
        },
        "attack": 7,
        "life": 30,
    },
    "axeman": {
        "name": "Axeman",
        "n": 0,
        "cost": {
            "food": 50,
            "metal": 15,
        },
        "attack": 10,
        "life": 25,
    },
    "swordsman": {
        "name": "Swordsman",
        "n": 0,
        "cost": {
            "food": 50,
            "wood": 5,
            "metal": 25,
        },
        "attack": 12,
        "life": 50,
    },
    "cavalry": {
        "name": "Cavalry",
        "n": 0,
        "cost": {
            "food": 200,
            "wood": 15,
            "metal": 25,
        },
        "attack": 15,
        "life": 80
    }
}

class Resources(GridLayout):
    food = NumericProperty(RESOURCES["food"])
    wood = NumericProperty(RESOURCES["wood"])
    stone = NumericProperty(RESOURCES["stone"])
    resources_list = ReferenceListProperty(food, wood, stone)

    def update(self, dt):
        # print()
        # print(dt)
        for i, resource in enumerate(self.resources_list):
            self.resources_list[i] += 1

class Units(GridLayout):
    villager = NumericProperty(UNITS["villager"]["n"])
    spearman = NumericProperty(UNITS["spearman"]["n"])
    axeman = NumericProperty(UNITS["axeman"]["n"])
    swordsman = NumericProperty(UNITS["swordsman"]["n"])
    cavalry = NumericProperty(UNITS["cavalry"]["n"])
    units_list = ReferenceListProperty(villager)

    def update(self, dt):
        # print()
        # print(dt)
        pass
    
    def recruit(self, unit, n):
        unit += n


class MainMenu(GridLayout):
    pass
    # rows = 1

    # def __init__(self, game):
    #     super(MainMenu, self).__init__()
    #     self.game = game
    #     self.add_widget(Button(on_release=self.game.change_to_menu_recruit()))
    #     self.add_widget(Button())

    # def change_to_menu_recruit(self):
    #     print("menu recruit")
    #     print(self.clear_widgets())
    #     self.game.add_widget(RecruitMenu())

class RecruitMenu(GridLayout):
    pass

class Game(GridLayout):
    resources = ObjectProperty(None)

    def update(self, dt):
        self.resources.update(dt)

    def change_to_menu_recruit(self):
        print("menu recruit")
        print(self.main_menu.clear_widgets())
        self.add_widget(RecruitMenu())
    

class RPGApp(App):
    def build(self):
        game = Game()
        # main_menu = GridLayout(cols=2)
        # main_menu.add_widget(Button())
        # main_menu.add_widget(Button())
        # game.add_widget(MainMenu(game))
        Clock.schedule_interval(game.update, 1.0/FPS)
        return game

if __name__ == "__main__":
    RPGApp().run()
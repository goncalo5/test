
from kivy.config import Config
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty, BooleanProperty, StringProperty


# BOXES = {
#     "offense": [
#         [
#             "attack damage": {
#                 "max": 2
#                 "child": ["armor penetration"]
#             },
#             "attack speed": {
#                 "max": 3,
#                 "child": ["range"]
#             }
#             "life steal": {
#                 "max": 3
#             }
#         ]
#     ],
        
#     },
#     "defense": {

#     }
# }


# BOXES = {
#     "offense": [
#         [
#             "attack damage": {
#                 "max": 3
#             },
#             "armor penetration": {
#                 "max": 2,
#             }
#             "life steal": {
#                 "max": 1
#             }
#         ],
#         [
#              {
#             "ability power": "max": 3
#             },
#             "magic penetration": {
#                 "max": 2,
#             },
#             "life steal": {
#                 "max": 1
#             }
#         ],
#         [
#             "attack speed": 
#         ]
#     ],
        
#     },
#     "defense": {

#     }
# }


BOXES = [
    [
        # level 1
        [
            "attack damage", "armor penetration", "life steal"
        ],
        [
            "ability power", "magic penetration", "spell vamp"
        ],
        [
            "attack speed", "critical"
        ]
    ],
    [
        # level 2

    ],
    [
        # level 3
        [
            "range"
        ]
    ]
]


N_COLS = 3
N_LINES = 3

class Box(Label):
    pass

class Game(Widget):
    
    def __init__(self, app):
        super().__init__()
        print("app.window.height", app.window.height)
        print("app.window.width", app.window.width)
        size_of_a_col = app.window.width / N_COLS
        size_of_a_line = app.window.height / N_LINES
        print("size_of_a_col", size_of_a_col)
        box_width = size_of_a_col
        box_height = size_of_a_line
        print("box_width", box_width)
        print("box_height", box_height)
        for line, level in enumerate(BOXES):
            print(line, "level", level)
            for col, box_label in enumerate(level):
                print("cols", col, "box_label", box_label)
                pos = (col * box_width, line * box_height)
                text = box_label[0]
                print("pos", pos)
                print("text", text)
                box = Box(pos=pos, text=text)
                # box.add_widget(Label(text=text))
                self.add_widget(box)
        # self.add_widget(Box(pos=(100, 100), text="ok"))


class Jogo_Do_DiogoApp(App):
    window = ObjectProperty(Window)
    # game = ObjectProperty(Game())
    n_cols = NumericProperty(N_COLS)
    n_lines = NumericProperty(N_LINES)

    def build(self):
        self.window.clearcolor = (0.3, 0, 0, 1)
        game = Game(self)
        return game


if __name__ == "__main__":
    Jogo_Do_DiogoApp().run()
from kivy.metrics import sp
from kivy.app import App
from kivy.core.window import Window
from kivy.clock import Clock
from kivy import properties as kp
from kivy.uix.widget import Widget
from kivy.animation import Animation

from collections import defaultdict
from random import randint
from random import uniform

SPRITE_SIZE = sp(20)
COLS = int(Window.width / SPRITE_SIZE)
ROWS = int(Window.height / SPRITE_SIZE)
print(COLS, ROWS)

LENGHT = 4
MOVESPEED = .1

ALPHA = 0.5

LEFT = "left"
UP = "up"
RIGHT = "right"
DOWN = "down"

direction_values = {
    LEFT: [-1, 0],
    UP: [0, 1],
    RIGHT: [1, 0],
    DOWN: [0, -1],
}

direction_group = {
    LEFT: "horizontal",
    UP: "vertical",
    RIGHT: "horizontal",
    DOWN: "vertical",
}
direction_keys = {
    "a": LEFT,
    "w": UP,
    "d": RIGHT,
    "s": DOWN
}
convert_code2key = {
    82: "w",
    79: "d",
    81: "s",
    80: "a"
}

class Sprite(Widget):
    coord = kp.ListProperty([0, 0])
    bgcolor = kp.ListProperty([0, 0, 0, 0])

SPRITES = defaultdict(lambda: Sprite())


class Fruit(Sprite):
    pass


class Snake(App):
    sprite_size = kp.NumericProperty(SPRITE_SIZE)

    head = kp.ListProperty([0, 0])
    snake = kp.ListProperty()  # list of list of coords
    lenght = kp.NumericProperty(LENGHT)

    fruit = kp.ListProperty([0, 0])
    fruit_sprite = kp.ObjectProperty(Fruit)

    direction = kp.StringProperty(RIGHT, options=(LEFT, UP, RIGHT, DOWN))
    buffer_direction = kp.StringProperty(RIGHT, options=(LEFT, UP, RIGHT, DOWN, ""))
    block_input = kp.BooleanProperty(False)

    alpha = kp.NumericProperty(0)
    rgba = kp.ListProperty([0, 0, 0, 0])

    def on_start(self):
        self.fruit_sprite = Fruit()
        self.fruit = self.new_fruit_location
        self.head = self.new_head_location
        Clock.schedule_interval(self.move, MOVESPEED)
        Window.bind(on_keyboard=self.key_handler)

    def on_fruit(self, *args):
        self.fruit_sprite.coord = self.fruit
        if not self.fruit_sprite.parent:
            self.root.add_widget(self.fruit_sprite)

    def key_handler(self, _, __, code, key, ____):
        # print(code, key, code in convert_code2key)
        try:
            if code in convert_code2key:
                key = convert_code2key[code]
                # print("key", key)
            self.try_change_direction(direction_keys[key])
        except KeyError:
            # print("KeyError")
            pass
    
    def try_change_direction(self, new_direction):
        # print("new_direction", new_direction)
        if direction_group[new_direction] != direction_group[self.direction]:
            if self.block_input:
                self.buffer_direction = new_direction
            else:
                self.direction = new_direction
                self.block_input = True

    def move(self, *args):
        # first add a new head in the current direction
        # print("move")
        self.block_input = False
        new_head =   [sum(x) for x in zip(self.head, direction_values[self.direction])]
        if not self.check_in_bounds(new_head) or new_head in self.snake:
            return self.die()
        if new_head == self.fruit:
            self.lenght += 1
            self.fruit = self.new_fruit_location
        if self.buffer_direction:
            self.try_change_direction(self.buffer_direction)
            self.buffer_direction = ""
        self.head = new_head

    def on_head(self, *args):
        # print("on_head", self.head)
        # second append the head to the snake
        self.snake = self.snake[-self.lenght:] + [self.head]
    
    def on_snake(self, *args):
        # print("on_snake", self.snake)
        # third draw the snake
        for index, coord in enumerate(self.snake):
            sprite = SPRITES[index]
            # print("coord", coord)
            sprite.coord = coord
            if not sprite.parent:
                self.root.add_widget(sprite)

    @property
    def new_head_location(self):
        return [randint(2, dim - 2) for dim in [COLS, ROWS]]

    @property
    def new_fruit_location(self):
        while True:
            fruit = [randint(0, dim - 1) for dim in [COLS, ROWS]]
            if fruit not in self.snake and fruit != self.fruit:
                print("fruit", fruit)
                return fruit
    
    def check_in_bounds(self, pos):
        return all(0 <= pos[x] < dim for x, dim in enumerate([COLS, ROWS]))
    
    def die(self):
        # print("die") 
        self.alpha = ALPHA
        Animation(alpha=0, duration=MOVESPEED).start(self)

        self.snake.clear()
        self.lenght = LENGHT
        self.root.clear_widgets()
        self.head = self.new_head_location
        self.fruit = self.new_fruit_location

if __name__ == "__main__":
    Snake().run()
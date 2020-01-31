from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty, BooleanProperty
from kivy.core.window import Window
from kivy.clock import Clock

FPS = 60
N_COLS = 8
JUMP = 1500
GRAVITY = 2500
FRICTION = 1
FORCE = 500


class Piece(Widget):
    is_touch =  BooleanProperty(False)
    vx = NumericProperty(0)
    ax = NumericProperty(0)
    vy = NumericProperty(0)

    def on_touch_down(self, touch):
        print("on_touch_down is_touch", self.is_touch)
        if self.collide_point(*touch.pos):
            self.is_touch = True

    def on_touch_move(self, touch):
        print("on_touch_move is_touch", self.is_touch)
        if self.is_touch:
            self.center = touch.pos

    def on_touch_up(self, touch):
        print("on_touch_up is_touch", self.is_touch)
        self.is_touch = False

class Game(Widget):
    piece = ObjectProperty(None)

    def __init__(self):
        super().__init__()
        self._keyboard = Window.request_keyboard(
            None, self, 'text')
        self._keyboard.bind(on_key_down=self._on_keyboard_down)
        self._keyboard.bind(on_key_up=self._on_keyboard_up)


    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        print("down", keyboard, keycode)
        if keycode[1] == "right":
            self.piece.vx += 100
            self.piece.ax += 100
        if keycode[1] == "left":
            self.piece.vx -= 100
            self.piece.ax -= 100
        if self.piece.y <= 20:
            if keycode[1] == "spacebar":
                self.piece.y += 50
                self.piece.vy -= JUMP
        

    def _on_keyboard_up(self, keyboard, keycode):
        print("up", keyboard, keycode)
        if keycode[1] == "right":
            self.piece.ax = 0
        if keycode[1] == "left":
            self.piece.ax = -0
        # if keycode[1] == "spacebar":
        #     self.piece.y += 200

    def update(self, dt):
        # print("update")
        print("before:", self.piece.pos, self.piece.vx, self.piece.ax)
        # self.piece.ax = 0
        self.piece.ax = -abs(self.piece.vx * FRICTION)

        # self.piece.ax += self.piece.vx * abs(FRICTION) * -1
        self.piece.vx += self.piece.ax * dt
        self.piece.x += self.piece.vx * dt + self.piece.ax * dt**2 / 2
        print("after:", self.piece.pos, self.piece.vx, self.piece.ax)


        # if self.piece.y > 0:
        #     self.piece.vy += GRAVITY * dt
        #     self.piece.y -= self.piece.vy * dt + GRAVITY * dt**2 / 2
        # else:
        #     self.piece.vy = 0

            # self.piece.vx += self.piece.ax * dt
            # self.piece.x += self.piece.vx * dt # + FORCE * dt**2 / 2
            # # Friction:
            # self.piece.x -= FRICTION * self.piece.vx * dt



class Damas2App(App):
    window = ObjectProperty(Window)
    n_cols = NumericProperty(N_COLS)
    
    def build(self):
        print(self.window.size)
        self.window.clearcolor = (0.2, 0.2, 0.2, 1)
        game = Game()
        Clock.schedule_interval(game.update, 1.0/FPS)
        return game


if __name__ == '__main__':
    Damas2App().run()
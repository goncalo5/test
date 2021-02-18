import random

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.animation import Animation
from kivy import properties as kp
from kivy.graphics import Rotate
from kivy.uix.label import Label
from 
# from kivy.atlas import Atlas
# atlas = Atlas('imgs/bird_anim/myatlas.atlas')

GRAVITY = 0.3
TIME_TO_RESPAWN_ANOTHER_PIPE = 3
DEBUG = 0
SPACE_BETEWEEN_PIPES = 200


class Sprite(Image): 
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size = self.texture_size


class Pipe(Widget):
    def __init__(self, pos):
        super().__init__(pos=pos)
        pipe_size = (100, 350)
        self.top_image = Sprite(source="imgs/obstacles/long.png")
        self.top_image.size = pipe_size
        self.top_image.pos = (self.x, self.y + SPACE_BETEWEEN_PIPES)  # 3.5 birds
        # self.top_image.pos = (self.x, self.y + 3.5 * 24)  # 3.5 birds
        self.add_widget(self.top_image)
        self.bottom_image = Sprite(source="imgs/obstacles/long.png")
        self.bottom_image.size = pipe_size
        # print(self.bottom_image.height, self.bottom_image.y)
        self.bottom_image.pos = (self.x, self.y - self.top_image.height)
        self.add_widget(self.bottom_image)

        if DEBUG:
            with self.top_image.canvas.after:
                Color(1,0,0,.7)
                self.top_image.rect = Rectangle(pos=self.top_image.pos, size=self.top_image.size)
            self.top_image.bind(pos=self.update_rect)
            with self.bottom_image.canvas.after:
                Color(1,0,0,.7)
                self.bottom_image.rect = Rectangle(pos=self.bottom_image.pos, size=self.bottom_image.size)
            self.bottom_image.bind(pos=self.update_rect)
            # print("y", self.y)
            print("pipe pos", self.pos)

        self.width = self.top_image.width
        self.scored = False

    def update_rect(self, *args):
        self.top_image.rect.pos = self.top_image.pos 
        self.bottom_image.rect.pos = self.bottom_image.pos 
    
    def update(self):
        # print(self.top_image.pos)
        self.x -= 2
        self.top_image.x = self.bottom_image.x = self.x
        if self.right < 0:
            self.parent.remove_widget


class Pipes(Widget):
    add_pipe = 0
    def update(self, dt):
        for child in list(self.children):
            child.update()
        self.add_pipe -= dt
        if self.add_pipe < 0:
            # y = 300
            y = random.randint(self.y + 50, self.height - 50 - SPACE_BETEWEEN_PIPES)
            self.add_widget(Pipe(pos=(self.width, y)))
            self.add_pipe = TIME_TO_RESPAWN_ANOTHER_PIPE


class Bird(Sprite):
    def __init__(self, pos):
        # super().__init__(source="imgs/bird_anim/frame-1.png", pos=pos)
        super().__init__(source="atlas://imgs/bird_anim2/up", pos=pos)
        self.size = (70, 70)
        with self.canvas.before:
            Rotate(angle=180, axis=(0, 1, 0), origin=self.center)
        if DEBUG:
            with self.canvas.after:
                Color(1,1,0,.5)
                self.rect = Rectangle(pos=self.pos, size=self.size)
            self.bind(pos=self.update_rect)
        self.velocity_y = 0
        self.gravity = -GRAVITY
    
    def update_rect(self, *args):
        self.rect.pos = self.pos 

    def update(self):
        self.velocity_y += self.gravity
        self.velocity_y = max(self.velocity_y, -10)
        self.y += self.velocity_y
        if self.velocity_y < 4:
            # print("up")
            self.source = "atlas://imgs/bird_anim2/up"
        elif self.velocity_y < 5:
            # print("down")
            self.source = "atlas://imgs/bird_anim2/mid-up"
        elif self.velocity_y < 5.5:
            # print("down")
            self.source = "atlas://imgs/bird_anim2/mid"

    def on_touch_down(self, *ignore):
        # print("touch")
        self.velocity_y = 5.5
        self.source = "atlas://imgs/bird_anim2/down"


class Background(Sprite):
    def __init__(self, source):
        super().__init__()
        self.image1 = Sprite(source=source)
        self.height = self.image1.height
        self.width = self.image1.width * 2
        self.image2 = Sprite(source=source, x=self.width / 2)
        self.image3 = Sprite(source=source, x=self.width)
        self.add_widget(self.image1)
        self.add_widget(self.image2)
        self.add_widget(self.image3)
        # self.image_dupe = Sprite(source=source, x=self.width)
        # self.add_widget(self.image_dupe)

    def update(self):
        self.image1.x -= 2
        self.image2.x -= 2
        self.image3.x -= 2
        # self.image_dupe.x -= 2
        if self.image1.right <= 0:
            self.image1.x = 0
            self.image2.x = self.width / 2
            self.image3.x = self.width
            # self.image_dupe.x = self.width


class Ground(Sprite):
    def __init__(self, source):
        super().__init__(source=source)
        # self.size = (966, 50)
        # self.y -= 0
    #     self.image = Sprite(source=source)
    #     self.add_widget(self.image)
    #     self.image.height = 50
    #     self.image.x = 0
        
    
    def update(self):
        self.x -= 2
        if self.x < -138:
            self.x += 138


class Game(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background = Background(source="imgs/backgrounds/bg.png")
        # print("background", self.background.size, Window.size)
        self.size = self.background.size
        # print("background", self.background.size, Window.size)
        self.add_widget(self.background)
        self.score_label = Label(center_x=self.center_x, top=self.top - 30, text="0")
        self.add_widget(self.score_label)
        self.ground = Ground(source="imgs/BrickPattern.png")
        self.pipes = Pipes(pos=(0, self.ground.height), size=self.size)
        self.add_widget(self.pipes)
        self.add_widget(self.ground)
        self.over_label = Label(center=self.center, opacity=0, text="Game Over")
        self.add_widget(self.over_label)
        self.bird = Bird(pos=(20, self.height / 2))
        self.add_widget(self.bird)
        Clock.schedule_interval(self.update, 1/60)
        self.game_over = False
        self.score = 0

    def update(self, dt):
        if self.game_over:
            return

        self.background.update()
        self.bird.update()
        self.ground.update()
        self.pipes.update(dt)

        if self.bird.collide_widget(self.ground):
            self.game_over = True

        for pipe in self.pipes.children:
            if pipe.top_image.collide_widget(self.bird):
                print("collide top", random.random())
                self.game_over = True
            if pipe.bottom_image.collide_widget(self.bird):
                self.game_over = True
                print("collide bot")
            elif not pipe.scored and pipe.right < self.bird.x:
                pipe.scored = True
                self.score += 1 
                self.score_label.text = str(self.score)
        if self.game_over:
            self.over_label.opacity = 1
            print("game over! score:", self.score)

class GameApp(App):
    def build(self):
        game = Game()
        # print("game", game.size, Window.size)
        Window.size = game.size
        # print("game", game.size, Window.size)
        return game

if __name__ == "__main__":
    GameApp().run()
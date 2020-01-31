<<<<<<< HEAD
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy import properties as kp

from kivy.vector import Vector

O = Vector(0, 0)
topright = Vector(1, 1)


print(topright)
print(O.distance(topright))
=======
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.image import Image
from kivy.graphics import Rotate
from kivy.uix.widget import Widget
from kivy.graphics import PopMatrix, PushMatrix
from kivy.graphics import Rectangle, Rotate, Color
from kivy.clock import Clock
from kivy import properties as kp
from kivy.core.window import Window
from kivy.vector import Vector


class Game(Widget):
    pass

class TestApp(App):
    current_frame = kp.NumericProperty(0)
    walking = kp.BooleanProperty(False)
    jumping = kp.BooleanProperty(False)
    left = kp.BooleanProperty(False)
    right = kp.BooleanProperty(False)

    def build(self):
        Window.bind(on_keyboard=self.key_handler)
        Clock.schedule_interval(self.update, .05)
        Clock.schedule_interval(self.update_anim, .3)
        self.load_images()
        self.game = Game()
        return self.game

    def load_images(self):
        self.standing_frames = ["bunny1_ready.png", "bunny1_stand.png"]
        self.walk_frames_r = ["bunny1_walk1.png", "bunny1_walk2.png"]
        self.walk_frames_l = []
        for frame in self.walk_frames_r:
            pass
        self.jump_frame = "bunny1_jump.png"
    
    def update(self, dt):
        print("update")
        player = self.game.player
        print("player.vel_x", player.vel_x)
        player.x += player.vel_x

    def update_anim(self, dt):
        player = self.game.player
        print(player.vel_x, player.x)
        if self.walking:
            print("animation walking")
            self.current_frame = (self.current_frame + 1) % len(self.walk_frames_r)
            if self.right:
                print("right")
                player.angle = 0
                player.source = self.walk_frames_r[self.current_frame]
            elif self.left:
                print("left")
                player.angle = 180
                player.source = self.walk_frames_r[self.current_frame]

        # show the idle animation
        if not self.walking and not self.jumping:
            # print("update animation")
            self.current_frame = (self.current_frame + 1) % len(self.standing_frames)
            self.game.player.source = self.standing_frames[self.current_frame]
        
        # self.walking = False
        # self.right = False
        # self.left = False
        # self.jumping = False

    def key_handler(self, _, __, code, key, ____):
        print(code, key)
        player = self.game.player
        convert_code2key = {
            82: "up",
            79: "right",
            81: "down",
            80: "left",
            44: "spacebar"
        }
        key = convert_code2key[code]
        if key == "up":
            player.vel_x = 0
            self.walking = False
        elif key == "down":
            player.vel_x = 0
            self.walking = False
        elif key == "left":
            player.vel_x = -3
            self.walking = True
            self.left = True
            self.right = False
        elif key == "right":
            player.vel_x = 3
            self.walking = True
            self.right = True
            self.left = False
        elif key == "spacebar":
            player.vel_x = 0
            self.jumping = True

if __name__ == '__main__':
    TestApp().run()
>>>>>>> 9565eb56c0ba5b732a9a1e06c45af17a1db22c7a

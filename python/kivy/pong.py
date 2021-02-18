from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from random import randint


class PongBall(Widget):

    # velocity of the ball on x and y axis
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)

    # referencelist property so we can use ball.velocity as
    # a shorthand, just like e.g. w.pos for w.x and w.y
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    # ``move`` function will move the ball one step. This
    #  will be called in equal intervals to animate the ball
    def move(self):
        self.pos = Vector(*self.velocity) + self.pos


class PongPaddle(Widget):

    score = NumericProperty(0)

    def bounce_ball(self, ball):
        if self.collide_widget(ball):
            # speedup  = 1.1
            # offset = 0.02 * Vector(0, ball.center_y - self.center_y)
            # ball.velocity =  speedup * (offset - ball.velocity)
            ball.velocity_x *= -1

class PongGame(Widget):
    ball = ObjectProperty(None)
    player1 = ObjectProperty(None)
    player2 = ObjectProperty(None)

    def on_touch_move(self, touch):
        if touch.x < self.width/3:
            self.player1.center_y = touch.y
        if touch.x > self.width - self.width/3:
            self.player2.center_y = touch.y

    def serve_ball(self, vel=(4, 0)):
        self.ball.center = self.center
        self.ball.velocity = Vector(10, 0).rotate(randint(0, 360))
        # self.ball2.center = self.center
        # self.ball2.velocity = Vector(8, 0).rotate(randint(0, 360))

    def update(self, dt):
        self.ball.move()
        # self.ball2.move()

        # bounce of paddles
        self.player1.bounce_ball(self.ball)
        self.player2.bounce_ball(self.ball)

        # print()
        # print (self.ball.x, self.ball.y)
        # print (self.ball2.x, self.ball2.y)

        # bounce off top and bottom
        if (self.ball.y < 0) or (self.ball.top > self.height):
            self.ball.velocity_y *= -1
        
        # went of to a side to score point?
        if self.ball.x < self.x:
            self.player2.score += 1
            self.serve_ball(vel=(4, 0))
        if self.ball.x > self.width:
            self.player1.score += 1
            self.serve_ball(vel=(-4, 0))

        # bounce off left and right
        # if (self.ball.x < 0) or (self.ball.right > self.width):
        #     self.ball.velocity_x *= -1

        # bounce off top and bottom
        # # if (self.ball2.y < 0) or (self.ball2.top > self.height):
            # self.ball2.velocity_y *= -1

        # bounce off left and right
        # # if (self.ball2.x < 0) or (self.ball2.right > self.width):
            # self.ball2.velocity_x *= -1
        
        # if abs(self.ball.y - self.ball2.y) < 50 and abs(self.ball.x - self.ball2.x) < 50:
        #     print("choque")
        #     if self.ball.x < self.ball2.x:
        #         if self.ball.velocity_x > 0:
        #             self.ball.velocity_x *= -1
        #         if self.ball2.velocity_x < 0:
        #             self.ball2.velocity_x *= -1
        #     if self.ball.x > self.ball2.x:
        #         if self.ball.velocity_x < 0:
        #             self.ball.velocity_x *= -1
        #         if self.ball2.velocity_x > 0:
        #             self.ball2.velocity_x *= -1
        #     if self.ball.y < self.ball2.y:
        #         if self.ball.velocity_y > 0:
        #             self.ball.velocity_y *= -1
        #         if self.ball2.velocity_y < 0:
        #             self.ball2.velocity_y *= -1
        #     if self.ball.y > self.ball2.y:
        #         if self.ball.velocity_y < 0:
        #             self.ball.velocity_y *= -1
        #         if self.ball2.velocity_y > 0:
        #             self.ball2.velocity_y *= -1



class PongApp(App):
    def build(self):
        game = PongGame()
        game.serve_ball()
        Clock.schedule_interval(game.update, 1.0/60.0)
        return game


if __name__ == '__main__':
    PongApp().run()
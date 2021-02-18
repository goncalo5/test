import kivy

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle, Point, GraphicException
from math import sqrt


def calculate_points(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dist = sqrt(dx * dx + dy * dy)
    o = []
    for i in range(1, int(dist)):
        mi = i / dist
        lastx = x1 + dx * mi
        lasty = y1 + dy * mi
        o.extend([lastx, lasty])
    return o


class Touchtracer(Widget):

    def on_touch_down(self, touch):
        ud = touch.ud
        ud['group'] = g = str(touch.uid)

        with self.canvas:
            ud['lines'] = [Point(points=(touch.x, touch.y), group=g)]

        print(touch)
        touch.grab(self)
        print(touch.grab_current)
        print(touch)

    def on_touch_move(self, touch):
        ud = touch.ud

        index = -1

        while True:
            try:
                points = ud['lines'][index].points
                oldx, oldy = points[-2], points[-1]
                break
            except:
                index -= 1

        points = calculate_points(oldx, oldy, touch.x, touch.y)

        if points:
            try:
                lp = ud['lines'][-1].add_point
                for idx in range(0, len(points), 2):
                    lp(points[idx], points[idx + 1])
            except GraphicException:
                pass
        print("grab_current", touch.grab_current)

    def on_touch_up(self, touch):
        print("grab_current", touch.grab_current)
        if touch.grab_current is self:
            touch.ungrab(self)
            ud = touch.ud
            self.canvas.remove_group(ud['group'])


class TouchtracerApp(App):

    def build(self):
        return Touchtracer()

    def on_pause(self):
        return True


if __name__ == '__main__':
    TouchtracerApp().run()

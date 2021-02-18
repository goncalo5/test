from kivy.core.window import Window
from kivy.clock import Clock
from kivy.vector import Vector

from settings import *

class Map(object):
    def __init__(self, filename, tilesize):
        self.data = []
        with open(filename, "rt") as f:
            for line in f:
                self.data.append(line.strip())
    
        self.tilewidth = len(self.data[0])
        self.tileheight = len(self.data)
        self.tilesize = tilesize
        self.width = self.tilewidth * self.tilesize
        self.height = self.tileheight * self.tilesize


class Camera:
    def __init__(self, width, height):
        self.offset = [0, 0]
        self.width = width
        self.height = height
        # self.first = first

    def update(self, target):
        x = -target.mapx + Window.width / 2
        y = -target.mapy + Window.height / 2
        # limit scrooling to map size:
        x = min(x, 0)  # left
        x = max(x, -(self.width - Window.width))  # right
        y = min(y, 0)  # bottom
        y = max(y, -(self.height - Window.height))  # top
        self.offset = [x, y]

    def apply(self, entity):
        # print("apply", entity, entity.x, entity.y, entity.mapx, entity.mapy)
        entity.center_x = entity.mapx + self.offset[0]
        entity.y = entity.mapy + self.offset[1]

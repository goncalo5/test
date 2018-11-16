from collections import *
from itertools import *
from time import *
from math import sqrt


class Point(object):

    def __init__(self, *args):
        if len(args) == 2:
            self.x = args[0]
            self.y = args[1]
        if len(args) == 1:
            try:
                self.x = args[0].x
                self.y = args[0].y
            except AttributeError:
                self.x = args[0][0]
                self.y = args[0][1]

    def dist(self, other):
        return sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

    def get_tuple(self):
        return (self.x, self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return 'Point(%s, %s)' % (self.x, self.y)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __radd__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __rsub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, number):
        return Point(self.x * number, self.y * number)

    def __rmul__(self, number):
        return Point(self.x * number, self.y * number)

    def __div__(self, number):
        return Point(self.x / number, self.y / number)

    def __rdiv__(self, number):
        return Point(self.x / number, self.y / number)

    def __floordiv__(self, number):
        return Point(self.x // number, self.y // number)

    def __rfloordiv__(self, number):
        return Point(self.x // number, self.y // number)

    def __neg__(self):
        return Point(-self.x, -self.y)


c1 = Point(0, 0)
c2 = Point(1, 1)
c3 = Point(1, 2)

# c3 = Point(c2)
# print c3


class Vector(object):
    def __init__(self, *args):
        try:
            points = [Point(arg) for arg in args]
        except TypeError:
            # 2 integers
            points = [Point((args[0], args[1]))]

        if len(points) == 2:
            points[0] = points[1] - points[0]
        elif len(points) > 2:
            raise Exception('Invalid Dimension!')
        self.x, self.y = points[0].get_tuple()

    def get_tuple(self):
        return self.x, self.y

    def length(self):
        return Point(0, 0).dist(Point(self.get_tuple()))

    def __repr__(self):
        return 'Vector(%s, %s)' % (self.x, self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return self.x != other.x or self.y != other.y

    def __lt__(self, other):
        return self.length() < other.length()

    def __le__(self, other):
        return self.length() <= other.length()

    def __gt__(self, other):
        return self.length() > other.length()

    def __ge__(self, other):
        return self.length() >= other.length()

    def add(self, other):
        try:
            x = self.x + other.x
            y = self.y + other.y
        except AttributeError:
            x = self.x + other[0]
            y = self.y + other[1]
            return Vector(x, y)
        print x, y
        if isinstance(other, Point):
            return Point(x, y)
        elif isinstance(other, Vector):
            return Vector(x, y)

    def __add__(self, other):
        return self.add(other)

    def __radd__(self, other):
        return self.add(other)


class Triangle(object):
    def __init__(self, *args):
        self.points = tuple(Point(arg) for arg in args)
        self.n = 3

    def calc_area(self):
        # |Sxiyi+1 + xny1 - Sxi+1yi -x1yn| / 2
        # |x1y2+x2y3+x3y1-y1x2-y2x3-y3x1| / 2
        soma = 0
        for i in range(self.n - 1):
            print 'x%sy%s' % (i, i + 1)
            r = self.points[i].x * self.points[i + 1].y
            print r
            soma += r
        soma += self.points[self.n - 1].x * self.points[0].y
        return soma

    def __repr__(self):
        return 'Triangle(%s, %s, %s)' % (self.points)


c1 = Point(0, 0)
c2 = Point(0, 1)
c3 = Point(1, 1)
v1 = Vector(0, 1)
v = []
# v.append(Vector(0, 1))


t1 = Triangle(c1, c2, c3)
print t1
print t1.calc_area()
t1 = Triangle(c3, c2, c1)
print t1
print t1.calc_area()

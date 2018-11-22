from collections import *
from itertools import *
from time import *
from math import sqrt


class Point(object):
    def __init__(self, *args):
        args = args if len(args) == 2 else args[0]

        try:
            self.x = args.x
            self.y = args.y
        except AttributeError:
            self.x = args[0]
            self.y = args[1]

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

c3 = Point(c2)
# print c3


class Edge(object):
    def __init__(self, *args):
        # print args
        args = args if len(args) == 2 else args[0]
        self.points = tuple(Point(arg) for arg in args)

    def length(self):
        return self.points[0].dist(self.points[1])

    def __repr__(self):
        return 'Edge(%s, %s)' % (self.points)

    def __eq__(self, other):
        if self.points == other.points or self.points[::-1] == other.points:
            return True
        return False


# print Edge(c1, c2) == Edge(Point(0, 0), Point(1, 1))
# print Edge(c1, c2).points
# print Edge(c1, c2).length()
# print Edge((c1, c2)).points
# print Edge((c1, c2)).length()


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
        if isinstance(other, Point):
            return Point(x, y)
        elif isinstance(other, Vector):
            return Vector(x, y)

    def __add__(self, other):
        return self.add(other)

    def __radd__(self, other):
        return self.add(other)


class Polygon(object):
    def __init__(self, *args):
        self.name = self.__class__.__name__
        print(self.name)
        self.vertices = list(Point(arg) for arg in args)

        self.calc_edges()
        self.calc_area()
        self.calc_perimeter()

    def calc_edges(self):
        self.edges = []
        for i in range(self.n):
            j = (i + 1) % self.n
            self.edges.append(Edge(self.vertices[i], self.vertices[j]))

    def calc_area(self):
        # |Sxiyi+1 + xny1 - Sxi+1yi -x1yn| / 2
        # |x1y2+x2y3+x3y1-y1x2-y2x3-y3x1| / 2
        soma = 0
        for i in range(self.n - 1):
            soma += self.vertices[i].x * self.vertices[i + 1].y
        soma += self.vertices[self.n - 1].x * self.vertices[0].y
        for i in range(self.n - 1):
            soma -= self.vertices[i + 1].x * self.vertices[i].y
        soma -= self.vertices[0].x * self.vertices[-1].y
        soma /= 2.
        self.area = abs(soma)

    def calc_perimeter(self):
        self.perimeter = sum(edge.length() for edge in self.edges)

    def __repr__(self):
        string = '%s, ' * self.n % tuple(self.vertices)
        return '%s(%s)' % (self.name, string[:-2])

    def __getitem__(self, index):
        return self.vertices[index]

    def __setitem__(self, index, value):
        print index
        print value
        self.vertices[index] = Point(value)

    def __add__(self, other):
        self.vertices = tuple(map(lambda vertice: vertice + other, self.vertices))
        self.calc_edges()
        return self


class Triangle(Polygon):
    n = 3

    def __init__(self, *args):
        super(Triangle, self).__init__(*args)


class Quadrilateral(Polygon):
    n = 4

    def __init__(self, *args):
        super(Quadrilateral, self).__init__(*args)


c1 = Point(0, 0)
c2 = Point(0, 1)
c3 = Point(1, 1)
c4 = Point(1, 0)
v1 = Vector(0, 1)
v = []
v.append(Vector(0, 1))


t1 = Triangle(c1, c2, c3)
print t1[0]
print t1[1]
print t1[2]
t1[0] = Point(1, 0)
print t1

# print(t1)
# print(t1.n)
# print(t1.area)
# print(t1.perimeter)

# t1 = Quadrilateral(c1, c2, c3, c4)
# print t1
#
# t1 = t1 + v1

# print(t1)
# print(t1.n)
# print(t1.area)
# print(t1.perimeter)

from collections import *
from itertools import *
from time import *
from math import sqrt, atan, pi


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

    def __hash__(self):
        return True

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

    def __abs__(self):
        return Point(abs(self.x), abs(self.y))


class Angle(object):
    def __init__(self, degrees=None, radians=None):
        if radians is None and degrees is None:
            raise Exception('Invalid Angle!')
        if radians is not None:
            self.radians = radians % (2 * pi)
            self.calc_degrees()
        elif degrees is not None:
            self.degrees = degrees % 360
            self.calc_radians()

    def calc_degrees(self):
        self.degrees = self.radians * 180 / pi

    def calc_radians(self):
        self.radians = self.degrees * pi / 180

    def __eq__(self, other):
        return self.radians == other.radians

    def __ne__(self, other):
        return self.radians != other.radians

    def __lt__(self, other):
        return self.radians < other.radians

    def __le__(self, other):
        return self.radians <= other.radians

    def __gt__(self, other):
        return self.radians > other.radians

    def __ge__(self, other):
        return self.radians >= other.radians

    def __repr__(self):
        return 'Angle(%s)' % self.degrees

    def __add__(self, other):
        return Angle(self.degrees + other.degrees)

    def __sub__(self, other):
        return Angle(self.degrees - other.degrees)

    def __mul__(self, other):
        return Angle(self.degrees * other)

    def __div__(self, other):
        return Angle(self.degrees / other)

    def __rmul__(self, other):
        return Angle(other * self.degrees)

    def __neg__(self):
        return Angle(-self.degrees)


class Edge(object):
    def __init__(self, *args):
        # print args
        args = args if len(args) == 2 else args[0]
        # print args
        try:
            self.points = args.points
        except AttributeError:
            self.points = tuple(Point(arg) for arg in args)

        self.calc_deltas()
        self.calc_length()
        self.calc_angle()

    def __repr__(self):
        return 'Edge(%s, %s)' % (self.points)

    def calc_deltas(self):
        self.dx = self.points[1].x - self.points[0].x
        self.dy = self.points[1].y - self.points[0].y

    def calc_length(self):
        self.length = self.points[0].dist(self.points[1])

    def calc_angle(self):
        if self.length <= 0:
            self.angle = None
        else:
            try:
                self.angle = Angle(radians=atan(self.dy / self.dx))
            except ZeroDivisionError:
                self.angle = Angle(90 if self.dy > 0 else -90)

    def __eq__(self, other):
        return set(self.points) == set(other.points)

    def __ne__(self, other):
        return set(self.points) != set(other.points)

    def __lt__(self, other):
        return self.length < other.length

    def __le__(self, other):
        return self.length <= other.length

    def __gt__(self, other):
        return self.length > other.length

    def __ge__(self, other):
        return self.length >= other.length


p00 = Point(0, 0)
p01 = Point(0, 1)
p11 = Point(1, 1)
e1 = Edge(p00, p01)
e2 = Edge(e1)
e3 = Edge(p00, p11)
# print e1 + e2
# print 5, Edge(p00, p01) >= Edge(p00, p11)


class Edges(object):
    def __init__(self, *args):
        self.edges = tuple(Edge(arg) for arg in args)

    def __repr__(self):
        string = '%s, ' * len(self.edges) % tuple(self.edges)
        return 'Edges(%s)' % (string[:-2])

    def __len__(self):
        return len(self.edges)


# for Edge:
def __add__(self, other):
    return Edges(self, other)


def __sub__(self, other):
    return Edges() if self == other else self


Edge.__add__ = __add__
Edge.__sub__ = __sub__
print e1 + e2
print e1 - e2
print e1 - e3

print Edges()
e1 = Edge(p00, p01)
e2 = Edge(p01, p11)
# print Edges(p00, p01)
print 11, Edges((p00, p01))
print 12, Edges(e1)
print 13, Edges(e1, e2)
print 14, Edges(e1, (p01, p11))


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

        self.calc_length()
        self.calc_angle()

    def __repr__(self):
        return 'Vector(%s, %s)' % (self.x, self.y)

    def get_tuple(self):
        return self.x, self.y

    def calc_length(self):
        self.length = Point(0, 0).dist(Point(self.get_tuple()))

    def calc_angle(self):
        if self.length <= 0:
            self.angle = None
        else:
            try:
                self.angle = Angle(radians=atan(self.y / self.x))
            except ZeroDivisionError:
                self.angle = Angle(90 if self.y > 0 else -90)

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
        self.vertices = list(Point(arg) for arg in args)

        self.calc_edges()
        self.calc_area()
        self.calc_perimeter()

    def __repr__(self):
        string = '%s, ' * self.n % tuple(self.vertices)
        return '%s(%s)' % (self.name, string[:-2])

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
        self.perimeter = sum(edge.length for edge in self.edges)

    def __getitem__(self, index):
        return self.vertices[index]

    def __setitem__(self, index, value):
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

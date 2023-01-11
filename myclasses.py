import math

class Point:
    """
    This is a class for defining Points in 2D space.
    Each point has an x coordinate and y coordinate.
    """

    # constructor method, creator of Point objects, instantiation
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "(%d, %d)" % (self.x, self.y)

    def __lt__(self, other):
        len = math.sqrt(self.x**2 + self.y**2)
        otherlen = math.sqrt(other.x**2 + other.y**2)
        return len < otherlen

class Rectangle:
    """
    This is to define rectangles in 2D.
    A rectangle is specified by the center Point, and its width, and its height.
    """

    def __init__(self, center, width, height):
        self.center = center
        self.width = width
        self.height = height

    def getArea(self):
        return self.width * self.height

    def __str__(self):
        return "centroid:%s, width: %d, height: %d" % (self.center, self.width, self.height)


centroid = Point(0, 0)
r = Rectangle(centroid, 1000, 200)

print(r.getArea())
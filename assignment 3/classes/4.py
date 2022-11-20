import math
class Point:
    def __init__(self, a,b):
        self.a = a
        self.b = b
    def show(self):
        print(self.a, self.b)

    def move(self, x, y):
        self.a, self.b = x, y

    def dist(self, d):
        return math.sqrt(((self.a - d.a)**2 + (self.b - d.b)**2))

# l = Point(1, 2)
# m = Point(4, 5)
# print(l.dist(m))

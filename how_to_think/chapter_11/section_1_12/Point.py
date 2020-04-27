class Point:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self, x=0, y=0):
        """ Create a new point at x,y. """
        self.x = x
        self.y = y

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y

    def __rmul__(self, other):
        return Point(other * self.x, other * self.y)

    def reverse(self):
        (self.x, self.y) = (self.y, self.x)

    def distance_from_origin(self):
        """ Compute my distance from the origin """
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def halfway(self, target):
        """ Return the halfway point between myself and the target """
        mx = (self.x + target.x) / 2
        my = (self.y + target.y) / 2
        return Point(mx, my)

    def reflect_x(self):
        return Point(self.x, -1 * self.y)

    def slope_from_origin(self):
        return self.y / self.x

    def get_line_to(self, target):
        delta_x = self.x - target.x
        delta_y = self.y - target.y

        slope = delta_y / delta_x
        y_intercept = self.y - (slope * self.x)

        return slope, y_intercept

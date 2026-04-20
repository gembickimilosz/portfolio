import turtle

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"Point({self.x}, {self.y})"


class Line:
    """
    Write an __eq__ method for the Line class that returns True if the Line objects 
    refer to Point objects that are equivalent, in either order.
    """
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __eq__(self, other):
        return (self.start == other.start and self.end == other.end) or \
               (self.start == other.end and self.end == other.start)

    """
    Write a Line method called midpoint that computes the midpoint of a line segment 
    and returns the result as a Point object.
    """
    def midpoint(self):
        mid_x = (self.start.x + self.end.x) / 2
        mid_y = (self.start.y + self.end.y) / 2
        return Point(mid_x, mid_y)

    def draw(self):
        t = turtle.Turtle()
        t.penup()
        t.goto(self.start.x, self.start.y)
        t.pendown()
        t.goto(self.end.x, self.end.y)

    def __str__(self):
        return f"Line({self.start}, {self.end})"


class Rectangle:
    def __init__(self, top_left, bottom_right):
        self.top_left = top_left
        self.bottom_right = bottom_right

    def make_lines(self):
        """Helper method to return the four sides of the rectangle as Line objects."""
        top_right = Point(self.bottom_right.x, self.top_left.y)
        bottom_left = Point(self.top_left.x, self.bottom_right.y)

        return [
            Line(self.top_left, top_right),
            Line(top_right, self.bottom_right),
            Line(self.bottom_right, bottom_left),
            Line(bottom_left, self.top_left)
        ]

    """
    Write a Rectangle method called midpoint that finds the point in the center of a 
    rectangle and returns the result as a Point object.
    """
    def midpoint(self):
        mid_x = (self.top_left.x + self.bottom_right.x) / 2
        mid_y = (self.top_left.y + self.bottom_right.y) / 2
        return Point(mid_x, mid_y)

    """
    Write a Rectangle method called make_cross that does the following:

    Uses make_lines to get a list of Line objects that represent the four sides of 
    the rectangle.
    Computes the midpoints of the four lines.
    Makes and returns a list of two Line objects that represent lines connecting 
    opposite midpoints, forming a cross through the middle of the rectangle.
    """
    def make_cross(self):
        lines = self.make_lines()
        midpoints = [line.midpoint() for line in lines]
        return [
            Line(midpoints[0], midpoints[2]),
            Line(midpoints[1], midpoints[3])
        ]

    def draw(self):
        for line in self.make_lines():
            line.draw()


class Circle:
    """
    Write a definition for a class named Circle with attributes center and radius,
    where center is a Point object and radius is a number. Include special methods 
    __init__ and a __str__, and a method called draw that uses jupyturtle functions 
    to draw the circle.
    """
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def __str__(self):
        return f"Circle(center={self.center}, radius={self.radius})"

    def draw(self):
        t = turtle.Turtle()
        t.penup()
        t.goto(self.center.x + self.radius, self.center.y)
        t.setheading(90)
        t.pendown()
        t.circle(self.radius)


if __name__ == "__main__":
    # Test Line equality and midpoint
    p1 = Point(0, 0)
    p2 = Point(100, 0)
    line1 = Line(p1, p2)
    line2 = Line(p2, p1)
    print("Lines equal (should be True):", line1 == line2)
    print("Line midpoint:", line1.midpoint())
    line1.draw()

    # Test Rectangle midpoint and cross
    rect = Rectangle(Point(-150, 100), Point(-50, 0))
    print("Rectangle midpoint:", rect.midpoint())
    cross = rect.make_cross()
    print("Cross lines:")
    for l in cross:
        print(l)

    # Draw rectangle and cross
    rect.draw()
    for l in cross:
        l.draw()

    # Draw Circle
    circle = Circle(Point(100, 50), 40)
    print(circle)
    circle.draw()

    turtle.done()
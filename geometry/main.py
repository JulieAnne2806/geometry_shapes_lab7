class Figure:
    def dimention(self):
        raise NotImplementedError("Цей метод має бути реалізований у підкласі")

    def perimetr(self):
        return None

    def square(self):
        return None

    def squareSurface(self):
        return None

    def squareBase(self):
        return None

    def height(self):
        return None

    def volume(self):
        raise NotImplementedError("Цей метод має бути реалізований у підкласі")

class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def dimention(self):
        return "2D"

    def perimetr(self):
        return self.a + self.b + self.c

    def square(self):
        p = self.perimetr() / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5

    def volume(self):
        return self.square()

class Rectangle(Figure):
    def __init__(self, a, b):
        self.a, self.b = a, b

    def dimention(self):
        return "2D"

    def perimetr(self):
        return 2 * (self.a + self.b)

    def square(self):
        return self.a * self.b

    def volume(self):
        return self.square()

class Trapeze(Figure):
    def __init__(self, a, b, side1, side2):
        self.a = a
        self.b = b
        self.side1 = side1
        self.side2 = side2

    def dimention(self):
        return "2D"

    def perimetr(self):
        return self.a + self.b + self.side1 + self.side2

    def square(self):
        return None

    def volume(self):
        return None

class Parallelogram(Figure):
    def __init__(self, base, side, height):
        self.base = base
        self.side = side
        self.height = height

    def dimention(self):
        return "2D"

    def perimetr(self):
        return 2 * (self.base + self.side)

    def square(self):
        return self.base * self.height

    def volume(self):
        return self.square()

class Circle(Figure):
    def __init__(self, r):
        self.r = r

    def dimention(self):
        return "2D"

    def perimetr(self):
        return 2 * 3.1415 * self.r

    def square(self):
        return 3.1415 * self.r ** 2

    def volume(self):
        return self.square()
class Ball(Figure):
    def __init__(self, r):
        self.r = r

    def dimention(self):
        return "3D"

    def squareSurface(self):
        return 4 * 3.1415 * self.r ** 2

    def volume(self):
        return 4/3 * 3.1415 * self.r ** 3

class TriangularPyramid(Figure):
    def __init__(self, a, h):
        self.a = a
        self.h = h

    def dimention(self):
        return "3D"

    def squareBase(self):
        return (self.a ** 2 * (3 ** 0.5)) / 49

    def height(self):
        return self.h

    def volume(self):
        return (1 / 3) * self.squareBase() * self.h

class QuadrangularPyramid(Figure):
    def __init__(self, a, b, h):
        self.a = a
        self.b = b
        self.h = h

    def dimention(self):
        return "3D"

    def squareBase(self):
        return self.a * self.b

    def height(self):
        return self.h

    def volume(self):
        return (1/3) * self.squareBase() * self.h

class RectangularParallelepiped(Figure):
    def __init__(self, a, b, h):
        self.a = a
        self.b = b
        self.h = h

    def dimention(self):
        return "3D"

    def squareSurface(self):
        return 2 * (self.a * self.b + self.a * self.h + self.b * self.h)

    def volume(self):
        return self.a * self.b * self.h

class Cone(Figure):
    def __init__(self, r, h):
        self.r = r
        self.h = h

    def dimention(self):
        return "3D"

    def squareBase(self):
        return 3.1415 * self.r ** 2

    def height(self):
        return self.h

    def squareSurface(self):
        l = (self.r ** 2 + self.h ** 2) ** 0.5
        return 3.1415 * self.r * l

    def volume(self):
        return (1/3) * self.squareBase() * self.h

class TriangularPrism(Figure):
    def __init__(self, a, b, c, h):
        self.a = a
        self.b = b
        self.c = c
        self.h = h

    def dimention(self):
        return "3D"

    def squareBase(self):
        p = (self.a + self.b + self.c) / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5

    def height(self):
        return self.h

    def volume(self):
        return self.squareBase() * self.h

def parse_figure(line):
    parts = line.strip().split()
    name = parts[0]
    values = list(map(float, parts[1:]))

    if name == "Triangle":
        return Triangle(*values)
    elif name == "Rectangle":
        return Rectangle(*values)
    elif name == "Trapeze":
        return Trapeze(*values)
    elif name == "Parallelogram":
        return Parallelogram(*values)
    elif name == "Circle":
        return Circle(*values)
    elif name == "Ball":
        return Ball(*values)
    elif name == "Cone":
        return Cone(*values)
    elif name == "TriangularPyramid":
        return TriangularPyramid(*values)
    elif name == "QuadrangularPyramid":
        return QuadrangularPyramid(*values)
    elif name == "RectangularParallelepiped":
        return RectangularParallelepiped(*values)
    elif name == "TriangularPrism":
        return TriangularPrism(*values)
    else:
        raise ValueError("Unknown figure type: " + name)


def is_valid_volume(v):
    return isinstance(v, (int, float)) and v is not None


if __name__ == "__main__":
    filename = "test_files/input01.txt"
    with open(filename, 'r') as f:
        figures = [parse_figure(line) for line in f if line.strip()]
    valid_figures = [fig for fig in figures if is_valid_volume(fig.volume())]
    if not valid_figures:
        print("Немає жодної фігури з обчислюваною площею або об'ємом.")
    else:
        max_figure = max(valid_figures, key=lambda fig: fig.volume())
        print("Фігура з найбільшою мірою:")
        print("Тип:", max_figure.__class__.__name__)
        print("Вимірність:", max_figure.dimention())
        print("Міра (площа або обʼєм):", round(max_figure.volume(), 2))

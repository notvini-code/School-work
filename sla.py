from math import sqrt, pi

class Circle:
    def __init__(self, r, x_centro, y_centro):
        self.r = r
        self.x_centro = x_centro
        self.y_centro = y_centro

    def pertence(self, x, y):
        distancia = sqrt((x - self.x_centro)**2 + (y - self.y_centro)**2)
        return distancia <= self.r

    def perimetro(self):
        return 2 * pi * self.r

    def area(self):
        return pi * (self.r ** 2)

if __name__ == "__main__":
    c1 = Circle(4, 0, 0)
    print(c1.perimetro())
    print(c1.area())
    print(c1.pertence(0, 1))
    print(c1.pertence(4, 0))

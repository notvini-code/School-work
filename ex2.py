class Domino:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def mostrar_pontos(self):
        print(f"Lado A: {self.a} | Lado B: {self.b}")

    def valor(self):
        return self.a + self.b

    def faces(self):
        return (self.a, self.b)

    def __str__(self):
        return f"Domino(A={self.a}, B={self.b})"


if __name__ == "__main__":
    d1 = Domino(2, 6)
    d1.mostrar_pontos()
    print(d1.valor())
    print(d1.faces())
    print(d1)

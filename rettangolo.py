class Rettangolo:
    def __init__(self, base, altezza):
        self.base = base
        self.altezza = altezza

    def area(self):
        area = self.base * self.altezza
        print(f"L'area del rettangolo è: {area}")

    def perimetro(self):
        perimetro = 2 * (self.base + self.altezza)
        print(f"Il perimetro del rettangolo è: {perimetro}")


# Esempio di utilizzo
r = Rettangolo(5, 3)
r.area()
r.perimetro()
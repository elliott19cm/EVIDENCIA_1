
class Operaciones:
    def _init_(self, x, y):
        self.x = x
        self.y = y

    def suma(self):
        return self.x + self.y

    def resta(self):
        return self.x - self.y

    def multiplicacion(self):
        return self.x * self.y

    def division(self):
        return self.x / self.y


if __name__ == "__main__":
    x = int(input("Ingrese el primer número: "))
    y = int(input("Ingrese el segundo número: "))

    operaciones = Operaciones(x, y)

    print("La suma es:", operaciones.suma())
    print("La resta es:", operaciones.resta())
    print("La multiplicación es:", operaciones.multiplicacion())
    print("La división es:", operaciones.division())
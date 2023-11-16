class Punto:

    def _init_(self, x, y):
        self.x = x
        self.y = y

    def imprimir(self):
        print("COORDENADAS DEL PUTO")
        print("(", self.x, ",", self.y, ")")

    def imprimir_cuadrante(self):
        if self.x > 0 and self.y > 0:
            print("Primer cuadrante")
        else:
            if self.x < 0 and self.y > 0:
                print("Segundo cuadrante")
            else:
                if self.x < 0 and self.y < 0:
                    print("Tercer Cuadrante")
                else:
                    if self.x > 0 and self.y < 0:
                        print("Cuarto Cuadrante")


# Bloque Principal
punto1 = Punto(10, -2)
punto1.imprimir()
punto1.imprimir_cuadrante()
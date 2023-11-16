class Edad:

    def inicializar(self, nom, edad):
        self.nombre = nom
        self.edad = edad

    def imprimir(self):
        print("NOMBRE", self.nombre)
        print("EDAD", self.edad)

    def mostrar_r(self):
        if self.edad >= 18:
            print("Es mayor de edad")
        else:
            print("Eres menor de edad")


# Bloque inicial
Edad1 = Edad()
Edad1.inicializar("elliott", 17)
Edad1.imprimir()
Edad1.mostrar_r()
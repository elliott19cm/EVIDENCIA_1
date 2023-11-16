class Alumno:
    def inicializar(self, nom, nota):
        self.nombre = nom
        self.nota = nota

    def imprimir(self):
        print("NOMBRE", self.nombre)
        print("NOTA", self.nota)

    def mostrar_r(self):
        if self.nota >= 4:
            print("Es aprobatorio")
        else:
            print("No es Aprobatorio")
# Bloque principal
Alumno1 = Alumno()
Alumno1.inicializar("elliott", 5)
Alumno1.imprimir()
Alumno1.mostrar_r()
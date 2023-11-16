class persona:
    def inicializar(self, nom):
        self.nombre = nom

    def imprimir(self):
        print("NOMBRE", self.nombre)


# bloque principal
persona1 = persona()
persona1.inicializar("Elliott")
persona1.imprimir()
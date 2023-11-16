class Empleado:

    def __init__(self):
        self.nombre = input("Ingresar el nombre del Empleado:")
        self.sueldo = float(input("Ingresar el sueldo:"))

    def imprimir(self):
        print("NOMBRE", self.nombre)
        print("SUELDO", self.sueldo)

    def muestra_r(self):
        if self.sueldo > 3000:
            print("Debe de pagar Impuestos")
        else:
            print("No debe de Pagar impuestos")


# Bloque Principal
Empleado1 = Empleado()
Empleado1.imprimir()
Empleado1.muestra_r()
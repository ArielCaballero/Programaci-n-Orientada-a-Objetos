import Manejadorflores
import Manejadorramos
import ramo

class menu:
    __switch=None
    def __init__(self):
        self.__switch={
            '1': self.opcion1,
            '2': self.opcion2,
            '3': self.opcion3,
            '0': self.salir
        }
    def getopcion(self, op, manejadorramo, manejadorflor):
        funcion=self.__switch.get(op, lambda:print("Opcion invalida"))
        if op=='1' or op=='2' or op=='3':
            funcion(manejadorramo, manejadorflor)
        else:
            funcion()
    def opcion1 (self, manejadorramo, manejadorflor):
        tamano=input("Ingrese un tamaño de ramo\n")
        ramos=ramo.ramo(tamano)
        print("Seleccione una flor por su numero, 0 para salir\n")
        manejadorflor.mostrarflores()
        opcion=input("\n")
        while opcion!='0':
            ramos.Agregarflor(manejadorflor.obtenerflor(int(opcion)))
            print(manejadorflor.obtenerflor(int(opcion)))
            print("Seleccione una flor por su numero, 0 para salir\n")
            manejadorflor.mostrarflores()
            opcion=input("\n")
        manejadorramo.Agregarramo(ramos)
    def opcion2(self, manejadorramo, manejadorflor):
        manejadorramo.mostrarfloresmasvendidas(manejadorflor)
    def opcion3(self, manejadorramo, manejadorflor):
        tamano=input("Ingrese un tamaño de ramo (pequeño, mediano, grande)\n")
        manejadorramo.mostrarflorentamano(tamano, manejadorflor)
    def salir():
        print("\nUsted salio del menu\n")
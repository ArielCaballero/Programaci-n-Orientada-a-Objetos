import PlanAhorro

class Menu:
    __switch=None
    def __init__(self):
        self.__switch={
            "1": self.opcion1,
            "2": self.opcion2,
            "3": self.opcion3,
            "4": self.opcion4,
            "0": self.salir
        }
    def opcion(self, op, listaplanes):
        funcion=self.__switch.get(op, lambda: print("Opcion invalida"))
        if (op=="1"  or op=="2" or op=="3" or op=="4"):
            funcion(listaplanes)
        else:
            funcion()
    def opcion1(self, listaplanes):
        listaplanes.Actualizarplanes()
    def opcion2(self, listaplanes):
        valor=float(input("Ingrese un valor\n"))
        listaplanes.MostrarMenores(valor)
    def opcion3(self, listaplanes):
        listaplanes.MostrarMontos()
    def opcion4(self, listaplanes):
        Nuevo_valor=int(input("Ingrese la nueva cantidad de cuotas necesarias para licitar\n"))
        PlanAhorro.setcuotasnecesarias(Nuevo_valor)
    def salir (self):
        print("Fin del Programa")
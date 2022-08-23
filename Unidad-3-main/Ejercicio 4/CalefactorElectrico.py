import Calefactor

class CalefactorElectrico(Calefactor.calefactor):
    __potencia=0
    def __init__(self, marca, modelo, potencia):
        if type(potencia)==int:
            super().__init__(marca, modelo)
            self.__potencia=potencia
        else:
            print("Error en la carga")
    def Calcularconsumo(self, costo, consumoporhora):
        if type(costo)==float and type(consumoporhora)==int:
            self.setconsumo(costo*consumoporhora*self.__potencia)
        else:
            print("Error en el calculo del consumo")
    def __str__(self):
        return ("{}\nPotencia:{}".format(super().__str__(), self.__potencia))
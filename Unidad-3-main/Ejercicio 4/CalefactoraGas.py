from Calefactor import calefactor

class CalefactoraGas(calefactor):
    __matricula=""
    __calorias=0
    def __init__(self, marca, modelo, matricula, calorias):
        if type(matricula)==str and type(calorias)==int:
            super().__init__(marca, modelo)
            self.__matricula=matricula
            self.__calorias=calorias
    def Calcularconsumo(self, metros, costo):
        if type(metros)==int and type(costo)==float:
            self.setconsumo(self.__calorias/1000*costo*metros)
        else: 
            print("Error en el calculo del consumo")
    def __str__(self):
        return ("{}\nmatricula: {}    Consumo:{}".format(super().__str__(), self.__matricula, self.__calorias))
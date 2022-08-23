class calefactor:
    __marca=""
    __modelo=""
    __consumo=0
    def __init__(self, marca, modelo):
        if (type(marca)==str and type(modelo)==str):
            self.__marca=marca
            self.__modelo=modelo
            self.__consumo=None
        else:
            print("Error en la carga de calefactor")
    def __str__(self):
        return ("Marca: {}    Modelo:{}".format(self.__marca, self.__modelo))
    def Calcularconsumo(self):
        pass
    def __lt__(self, otro):
        valor=None
        if type(otro)==type(self):
            valor=(self.getconsumo()<otro.getconsumo())
        else:
            print("Error en comparacion, son tipos de datos distintos")
        return(valor)
    def getconsumo(self):
        return (self.__consumo)
    def setconsumo(self, consumo):
        self.__consumo=consumo
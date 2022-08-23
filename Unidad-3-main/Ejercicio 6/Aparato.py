class Aparato:
    __marca=""
    __modelo=""
    __color=""
    __pais=""
    __preciobase=0
    __importe=""
    def __init__(self, marca, modelo, color, pais, precio):
        if type(marca)==str and type(modelo)==str and type(color)==str and type(pais)==str and type(precio)==float:
            self.__color=color
            self.__marca=marca
            self.__modelo=modelo
            self.__pais=pais
            self.__preciobase=precio
            self.__importe=self.__preciobase
        else:
            print("Error en la carga")
    def getmarca(self):
        return self.__marca
    def getmodelo(self):
        return self.__modelo
    def getpais(self):
        return self.__pais
    def getcolor(self):
        return self.__color
    def getprecio(self):
        return self.__preciobase
    def setimporte(self, importe):
        self.__importe=importe
    def getimporte(self):
        return(self.__importe)
    def calcularimporte(self):
        pass
    def toJSON(self):
        pass
    def __str__(self):
        return("Marca: {}   Pais: {}    Importe: {}".format(self.__marca, self.__pais, self.__importe))
from Aparato import Aparato

class Heladera(Aparato):
    __capacidad=""
    __freezer=""
    __ciclica=""
    def __init__(self, marca, modelo, color, pais, precio, capacidad, freezer, ciclica):
        if type(capacidad)==str and type(freezer)==bool and type(ciclica)==bool:
            super().__init__(marca, modelo, color, pais, precio)
            self.__capacidad=capacidad
            self.__freezer=freezer
            self.__ciclica=ciclica
        else:
            print("Error en la carga de Heladera")
    def calcularimporte(self):
        valor=1
        if (self.__freezer):
            valor+=0.05
        else:
            valor+=0.01
        if (self.__ciclica):
            valor+=0.1
        self.setimporte(self.getprecio()*valor)
    def toJSON(self):
        d=dict(__class__=self.__class__.__name__, __atributos__=dict(marca=self.getmarca(), modelo=self.getmodelo(), color=self.getcolor(), pais=self.getpais(), precio=self.getprecio(), capacidad=self.__capacidad, freezer=self.__freezer, ciclica=self.__ciclica))
        return d
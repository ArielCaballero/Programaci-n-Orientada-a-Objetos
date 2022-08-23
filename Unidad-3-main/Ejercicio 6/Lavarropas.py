from Aparato import Aparato

class Lavarropas(Aparato):
    __capacidad=""
    __velocidad=""
    __cantidadprogramas=""
    __carga=""
    def __init__(self, marca, modelo, color, pais, precio, capacidad, velocidad, cantidadprogramas, carga):
        if (type(capacidad)==int and type(velocidad)==str and type(cantidadprogramas)==str and type(carga)==str):
            super().__init__(marca, modelo, color, pais, precio)
            self.__capacidad=capacidad
            self.__cantidadprogramas=cantidadprogramas
            self.__velocidad=velocidad
            self.__carga=carga
        else:
            print("Error en la carga de heladeras")
    def calcularimporte(self):
        valor=1
        if (self.__capacidad<=5):
            valor+=0.01
        else:
            valor+=0.03
        self.setimporte(self.getprecio()*valor)
    def getcarga(self):
        return self.__carga
    def toJSON(self):
        d=dict(__class__=self.__class__.__name__, __atributos__=dict(marca=self.getmarca(), modelo=self.getmodelo(), color=self.getcolor(), pais=self.getpais(), precio=self.getprecio(), capacidad=self.__capacidad, velocidad=self.__velocidad, cantidadprogramas=self.__cantidadprogramas, carga=self.__carga))
        return d
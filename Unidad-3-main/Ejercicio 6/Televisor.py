from Aparato import Aparato

class Televisor(Aparato):
    __tipopantalla=""
    __pulgadas=""
    __definicion=""
    __conexion=""
    def __init__(self, marca, modelo, color, pais, precio, tipopantalla, pulgadas, definicion, conexion):
        if type(tipopantalla)==str and type(pulgadas)==str and type(definicion)==str and type(conexion)==bool:
            super().__init__(marca, modelo, color, pais, precio)
            self.__tipopantalla=tipopantalla
            self.__pulgadas=pulgadas
            self.__definicion=definicion
            self.__conexion=conexion
        else:
            print("Error en carga de televisor")
    def calcularimporte(self):
        valor=1
        if (self.__definicion=="SD"):
            valor+=0.01
        elif (self.__definicion=="HD"):
            valor+=0.02
        elif (self.__definicion=="FULL HD"):
            valor+=0.03
        if (self.__conexion):
            valor+=0.01
        self.setimporte(self.getprecio()*valor)
    def toJSON(self):
        d=dict(__class__=self.__class__.__name__, __atributos__=dict(marca=self.getmarca(), modelo=self.getmodelo(), color=self.getcolor(), pais=self.getpais(), precio=self.getprecio(), tipopantalla=self.__tipopantalla, pulgadas=self.__pulgadas, definicion=self.__definicion, conexion=self.__conexion))
        return d
class flor:
    __numero=0
    __nombre=""
    __color=""
    __descripcion=""
    def __init__(self, nombre, color, descripcion, numero):
        if type(nombre)==str and type(color)==str and type(descripcion)==str and type(numero)==int:
            self.__nombre=nombre
            self.__color=color
            self.__descripcion=descripcion
            self.__numero=numero
        else:
            print("Error en la carga de una flor")
    def getnombre(self):
        return self.__nombre
    def getcolor(self):
        return(self.__color)
    def getdescripcion(self):
        return(self.__descripcion)
    def __str__(self):
        return("{} {}: {}".format(self.getnombre(), self.getcolor(), self.getdescripcion()))
    def getnumero(self):
        return self.__numero
    '''def __gt__(self, otro):
        valor=None
        if type(otro)==type(self):
            valor=self.getnumero()>otro.getnumero()
        return(valor)'''
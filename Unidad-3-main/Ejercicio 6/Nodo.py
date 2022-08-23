from Aparato import Aparato

class Nodo:
    __Aparato=None
    __siguiente=None
    def __init__(self, aparat):
        if isinstance(aparat, Aparato):
            self.__Aparato=aparat
            self.__siguiente=None
        else:
            print ("Error al crear un nodo")
    def setsiguiente(self, siguiente):
        self.__siguiente=siguiente
    def getsiguiente(self):
        return self.__siguiente
    def getAparato(self):
        return(self.__Aparato)
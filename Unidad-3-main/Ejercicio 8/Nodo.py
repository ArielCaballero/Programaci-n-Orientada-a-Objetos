import Personal

class Nodo:
    __siguiente=None
    __dato=None
    def __init__(self, persona):
        if (isinstance(persona, Personal.Personal)):
            self.__dato=persona
            self.__siguiente=None
        else:
            print("Error en ingreso de datos al nodo")
    def getsiguiente(self):
        return (self.__siguiente)
    def setsiguiente(self, siguiente):
        self.__siguiente=siguiente
    def getdato(self):
        return self.__dato
import flor

class ramo:
    __tamaño=""
    __Listaflores=[]
    def __init__(self, tamaño):
        if type(tamaño)==str:
            self.__tamaño=tamaño
            self.__Listaflores=[]
        else:
            print("Error en carga")
    def gettamano(self):
        return(self.__tamaño)
    def Agregarflor(self, flores):
        if type(flores)==flor.flor:
            self.__Listaflores.append(flores)
    def buscarflores(self, numeroflor):
        cantidad=0
        for flores in self.__Listaflores:
            if flores.getnumero()==numeroflor:
                cantidad+=1
        return cantidad
    def encontrarflor(self, numeroflor):
        resultado=False
        i=0
        while (i<len(self.__Listaflores) and self.__Listaflores[i].getnumero()!=numeroflor):
            i+=1
        if i<len(self.__Listaflores):
            resultado=True
        return(resultado)
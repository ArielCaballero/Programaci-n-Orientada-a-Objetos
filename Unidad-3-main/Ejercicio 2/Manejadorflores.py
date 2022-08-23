import numpy

import flor

class manejadorflores:
    __lista=[]
    __dimension=0
    __cantidad=0
    __incremento=0
    def __init__(self, dimension=0, incremento=2):
        self.__dimension=dimension
        self.__cantidad=0
        self.__incremento=incremento
        self.__lista=numpy.empty(self.__dimension, dtype=flor.flor)
    def getcantidad(self):
        return self.__cantidad
    def Agregarflor(self, flores):
        if type(flores)==flor.flor:
            if self.__cantidad==self.__dimension:
                self.__dimension+=self.__incremento
                self.__lista.resize(self.__dimension)
            self.__lista[self.__cantidad]=flores
            self.__cantidad+=1
        else:
            print ("Error en la carga del manejadorflores")
    '''def ordenar(self):
        self.__lista.sort()'''
    def mostrarflores(self):
        for i in range(self.__cantidad):
            print ("{}_ {}".format(self.__lista[i].getnumero(),self.__lista[i]))
    def getlista(self):
        return self.__lista
    def getflor (self, indice):
        return (self.__lista[indice])
    def buscarflor(self, flores):
        valor=None
        if type(flores)==flor.flor:
            valor=False
            i=0
            while (i<len(self.__lista) and valor==False):
                if self.__lista!=flores:
                    valor=True
                i=i+1
        return valor
    def obtenerflor(self, numero):
        valor=None
        if type(numero)==int:
            i=0
            while (i<len(self.__lista) and self.__lista[i].getnumero()!=numero):
                i+=1
            if i<len(self.__lista):
                valor=self.__lista[i]
        return(valor)
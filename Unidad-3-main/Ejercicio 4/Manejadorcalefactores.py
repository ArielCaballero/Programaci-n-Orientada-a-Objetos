import numpy

import Calefactor
from CalefactorElectrico import CalefactorElectrico
from CalefactoraGas import CalefactoraGas

class Manejadorcalefactores:
    __Lista=[]
    __cantidad=0
    __dimension=0
    __incremento=0
    def __init__(self, dimension, incremento=5):
        self.__dimension=dimension
        self.__incremento=incremento
        self.__cantidad=0
        self.__Lista=numpy.empty(self.__dimension, dtype=Calefactor.calefactor)
    def Agregarcalefactor(self, calefactores):
        if (self.__cantidad==self.__dimension):
            self.__dimension+=self.__incremento
            self.__Lista.resize(self.__dimension)
        self.__Lista[self.__cantidad]=calefactores
        self.__cantidad+=1
    def calcularconsumoelectricos(self):
        costo=float(input("Ingrese el costo de kilowatt/h\n"))
        estimacion=int(input("Ingrese el consumo estimado\n"))
        for i in range(self.__cantidad):
            if isinstance(self.__Lista[i], CalefactorElectrico):
                self.__Lista[i].Calcularconsumo(costo, estimacion)
    def calcularconsumoagas(self):
        costo=float(input("Ingrese el costo por metro cubico\n"))
        metro=int(input("Ingrese cantidad que se estima consumir en metro cubico\n"))
        for i in range(self.__cantidad):
            if isinstance(self.__Lista[i], CalefactoraGas):
                self.__Lista[i].Calcularconsumo(metro, costo)
    def menorelectrico(self):
        bandera=True
        for calefactores in self.__Lista:
            if isinstance(calefactores, CalefactorElectrico):
                if bandera:
                    valor=calefactores
                    bandera=not bandera
                else:
                    if calefactores<valor:
                        valor=calefactores
        return(valor)
    def menoragas(self):
        bandera=True
        for i in range(self.getcantidad()):
            if isinstance(self.__Lista[i], CalefactoraGas):
                if bandera:
                    valor=self.__Lista[i]
                    bandera=not bandera
                else:
                    if self.__Lista[i]<valor:
                        valor=self.__Lista[i]
        return(valor)
    def menor(self):
        valor=self.__Lista[0]
        for calefactores in self.__Lista:
            if isinstance(calefactores, CalefactorElectrico) and calefactores<valor:
                valor=calefactores
        return(valor)
    def getcantidad(self):
        return self.__cantidad
    def printear(self):
        for lista in self.__Lista:
            print (lista)
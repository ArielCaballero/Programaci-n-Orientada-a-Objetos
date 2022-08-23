import numpy

import equipo
import contrato

class manejadorequipos:
    __Lista=[]
    __dimension=0
    __incremento=0
    __cantidad=0
    def __init__(self, dimension, incremento=3):
        if type(dimension)==int:
            self.__dimension=dimension
            self.__cantidad=0
            self.__incremento=incremento
            self.__Lista=numpy.empty(self.__dimension, dtype=equipo.equipo)
        else:
            print("Error crear manejador equipos")
    def agregarequipo(self, equi):
        if type(equi)==equipo.equipo:
            if self.__cantidad==self.__dimension:
                self.__dimension+=self.__incremento
                self.__Lista.resize(self.__dimension)
            self.__Lista[self.__cantidad]=equi
            self.__cantidad+=1
        else:
            print("Error en tipo de dato al agregar equipo a manejador")
    def vencimientosequipo(self, identificador):
        self.__Lista[identificador-1].listarvencimientos()
    def buscarequipo (self, nombre):
        valor=None
        i=0
        band=True
        while(i<self.__cantidad and band):
            if self.__Lista[i].getnombre()==nombre:
                band= not band
            i+=1
        if not band:
            valor=self.__Lista[i-1]
        return valor
    def calcularimportes (self, nombre):
        equi=self.buscarequipo(nombre)
        if equi!=None:
            equi.calcularcontratos()
        
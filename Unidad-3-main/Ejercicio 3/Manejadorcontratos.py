import numpy

import contrato
import jugador
import equipo

class manejadorcontratos:
    __Lista=[]
    __dimension=0
    __incremento=0
    __cantidad=0
    def __init__(self, dimension=0, incremento=3):
        if type(dimension)==int:
            self.__dimension=dimension
            self.__cantidad=0
            self.__incremento=incremento
            self.__Lista=numpy.empty(self.__dimension, dtype=contrato.contrato)
        else:
            print("Error crear manejador contratos")
    def agregarcontrato(self, contrat):
        if type(contrat)==contrato.contrato:
            if self.__cantidad==self.__dimension:
                self.__dimension+=self.__incremento
                self.__Lista.resize(self.__dimension)
            self.__Lista[self.__cantidad]=contrat
            self.__cantidad+=1
        else:
            print("Error en tipo de dato al agregar equipo a manejador contratos")
    def mostrarjugadorpordni(self, dni):
        bandera=True
        i=0
        while (i<self.__cantidad) and bandera:
            if self.__Lista[i].getjugador().getdni()==dni:
                bandera=not bandera
            i+=1
        if not bandera:
            print("Equipo:{}\nFecha de finalizacion: {}".format(self.__Lista[i-1].getequipo(), self.__Lista[i-1].getfin()))
    
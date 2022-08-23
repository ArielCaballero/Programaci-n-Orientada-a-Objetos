import datetime

import contrato

class equipo:
    __nombre="" 
    __ciudad=""
    __contratos=[]
    def __init__(self, nombre, ciudad):
        if type(nombre)==str and type(ciudad)==str:
            self.__ciudad=ciudad
            self.__nombre=nombre
            self.__contratos=[]
        else:
            print("Error en crear equipo")
    def firmarcontrato(self, jugado, fechaincio, fechafin, pago):
        contratofirmado=contrato.contrato(jugado, self, fechaincio, fechafin, pago)
        self.__contratos.append(contratofirmado)
        return contratofirmado
    def __str__(self):
        return(self.__nombre + " de " + self.__ciudad)
    def listarvencimientos(self):
        for contrat in self.__contratos: 
            if contrat.mesesalvencimiento()<=6:
                print(contrat.getjugador())
    def getnombre(self):
        return self.__nombre
    def calcularcontratos(self):
        total=0
        i=0
        for cont in self.__contratos:
            total+=cont.calcularimporte()
            print ("Jugador: {}    Importe: {}".format(cont.getjugador().getnombre(), cont.calcularimporte()))
        print("Total de los importes: {}".format(total))

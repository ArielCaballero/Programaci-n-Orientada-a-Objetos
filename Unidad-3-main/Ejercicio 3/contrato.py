import datetime

import jugador
import equipo

class contrato:
    __jugador=""
    __equipo=""
    __fechainicio=""
    __fechafin=""
    __pagomensual=0
    def __init__(self, jugado, equip, inicio, fin, pago):
        if (type(jugado)==jugador.jugador and type(equip)==equipo.equipo and type(inicio)==str and type(fin)==str and type(pago)==float):
            self.__jugador=jugado
            self.__equipo=equip
            self.__fechainicio=inicio
            self.__fechafin=fin
            self.__pagomensual=pago
        else:
            print("Error en carga de contrato")
    def getjugador(self):
        return self.__jugador
    def getequipo(self):
        return self.__equipo
    def getfin(self):
        return self.__fechafin
    def getpago(self):
        return self.__pagomensual
    def mesesalvencimiento(self):
        mes=0
        fecha=self.getfin().split("/")
        mesfin=int(fecha[1])
        actual=datetime.date.today()
        mesactual=int(actual.month)+12*(int(actual.year)-int(fecha[2]))
        mes=mesfin-mesactual
        return mes
    def calcularimporte(self):
        importe=0
        if self.mesesalvencimiento()>0:
            importe=self.mesesalvencimiento()*self.getpago()
        return importe

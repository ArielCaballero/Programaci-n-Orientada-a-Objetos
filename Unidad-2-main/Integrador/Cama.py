from time import strftime
import datetime

class cama:
    __habitacion=0
    __estado=False
    __paciente=None
    __diagnostico=None
    __fechainternacion=None
    __fechaalta=None
    def __init__(self, habitacion=None, estado=False, paciente=None, diagnostico=None, fechaint=None, fechalta=None):
        if ((type(habitacion)==int)and (type(estado)==str) and (type(paciente)==str)and (type(diagnostico)==str)and (type(fechaint)==str)):
            self.__habitacion=habitacion
            if estado=="False":
                self.__estado=not(bool(estado))
            else:
                self.__estado=bool(estado)
            self.__paciente=paciente
            self.__diagnostico=diagnostico
            self.__fechainternacion=fechaint
            self.__fechaalta=None
        else:
            if (habitacion==None and estado==False and paciente==None and diagnostico==None and fechaint==None and fechalta==None):
                self.__habitacion=habitacion
                self.__estado=estado
                self.__paciente=paciente
                self.__diagnostico=diagnostico
                self.__fechainternacion=fechaint
                self.__fechaalta=None
            else:
                print("Datos no validos para cama")
    def setfechaalta(self):
        fecha=datetime.date.today().strftime('%d/%m/%Y')
        self.__fechaalta=fecha
    def getpaciente(self):
        return(self.__paciente)
    def gethabitacion(self):
        return(self.__habitacion)
    def getdiagnostico(self):
        return(self.__diagnostico)
    def getfechainternacion(self):
        return(self.__fechainternacion)
    def getfechaalta(self):
        return(self.__fechaalta)
    def __str__(self):
        return("Paciente: {}\t\tHabitacion: {}\nDiagnostico: {}\tFecha de Internacion: {}\n Fecha de Alta: {}".format(self.__paciente,self.__habitacion,self.__diagnostico,self.__fechainternacion,self.__fechaalta))
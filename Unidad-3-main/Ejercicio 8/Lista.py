from zope.interface import implementer

from DocenteInvestigador import DocenteInvestigador
from PersonaldeApoyo import PersonaldeApoyo
from Docente import Docente
import Interface
import Tesorero
import Director
import Nodo
import Personal

@implementer(Tesorero.ITesorero)
@implementer(Director.IDirector)
@implementer(Interface.Interfaceejemplo)
class Lista:
    __comienzo=None
    __actual=None
    __indice=0
    __tope=0
    def __init__(self):
        self.__comienzo=None
        self.__actual=None
        self.__indice=0
        self.__tope=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.__indice==self.__tope:
            self.__actual=self.__comienzo
            self.__indice=0
            raise StopIteration
        else:
            self.__indice+=1
            dato=self.__actual.getdato()
            self.__actual=self.__actual.getsiguiente()
            return (dato)
    def AgregarElemento(self, elemento):
        nodito=Nodo.Nodo(elemento)
        nodito.setsiguiente(self.__comienzo)
        self.__comienzo=nodito
        self.__actual=nodito
        self.__tope+=1
    def InsertarElemento(self, elemento, posicion):
        self.__actual=self.__comienzo
        self.__indice=0
        if posicion == 0:
            self.AgregarElemento(elemento)
        else:
            while (self.__indice!=posicion and self.__actual!=None):
                ant=self.__actual
                self.__actual=self.__actual.getsiguiente()
                self.__indice+=1
            if self.__indice==posicion:
                nuevonodo=Nodo.Nodo(elemento)
                nuevonodo.setsiguiente(self.__actual)
                ant.setsiguiente(nuevonodo)
                self.__tope+=1
                self.__indice=0
                self.__actual=self.__comienzo
            else:
                raise IndexError
   
    def MostrarElemento(self, posicion):
        valor=None
        if self.__tope<=posicion or posicion<0:
            raise IndexError
        else:
            self.__actual=self.__comienzo
            self.__indice=0
            while (self.__indice!=posicion):
                self.__actual=self.__actual.getsiguiente()
                self.__indice+=1
            valor= type(self.__actual.getdato())
        return valor
    
    def modificarBasico (self, dni, nuevobasico):
        self.__actual=self.__comienzo
        self.__indice=0
        bandera=True
        while (self.__indice<self.__tope and bandera):
            if self.__actual.getdato().getdni()==dni:
                bandera= not bandera
            else:
                self.__actual=self.__actual.getsiguiente()
                self.__indice+=1
        if not bandera:
            self.__actual.getdato().modificarbasico(nuevobasico)
        self.__actual=self.__comienzo
        self.__indice=0
    
    def modificarImporteExtra (self, dni, nuevoimporteextra):
        self.__actual=self.__comienzo
        self.__indice=0
        bandera=True
        while (self.__indice<self.__tope and bandera):
            if self.__actual.getdato().getdni()==dni:
                bandera= not bandera
            else:
                self.__actual=self.__actual.getsiguiente()
                self.__indice+=1
        if not bandera:
            if type(self.__actual.getdato()==DocenteInvestigador):
                self.__actual.getdato().modificarImporteExtra(nuevoimporteextra)
            else:
                print("El agente no es un docente investigador")
        self.__actual=self.__comienzo
        self.__indice=0

    def modificarPorcentajeporcargo (self, dni, nuevoporcentaje):
        self.__actual=self.__comienzo
        self.__indice=0
        bandera=True
        while (self.__indice<self.__tope and bandera):
            if self.__actual.getdato().getdni()==dni:
                bandera= not bandera
            else:
                self.__actual=self.__actual.getsiguiente()
                self.__indice+=1
        if not bandera:
            if type(self.__actual.getdato()==Docente):
                self.__actual.getdato().modificarporcentaje(nuevoporcentaje)
            else:
                print("El agente no es un docente")
        self.__actual=self.__comienzo
        self.__indice=0
    
    def modificarPorcentajeporcategoria (self, dni, nuevoporcentaje):
        self.__actual=self.__comienzo
        self.__indice=0
        bandera=True
        while (self.__indice<self.__tope and bandera):
            if self.__actual.getdato().getdni()==dni:
                bandera= not bandera
            else:
                self.__actual=self.__actual.getsiguiente()
                self.__indice+=1
        if not bandera:
            if type(self.__actual.getdato()==PersonaldeApoyo):
                self.__actual.getdato().modificarporcentaje(nuevoporcentaje)
            else:
                print("El agente no es personal de apoyo")
        self.__actual=self.__comienzo
        self.__indice=0

    def gastosSueldoPorEmpleado(self, dni):
        valor=None
        self.__actual=self.__comienzo
        self.__indice=0
        bandera=True
        while (self.__indice<self.__tope and bandera):
            if self.__actual.getdato().getdni()==dni:
                print ("Sueldo: {}".format(self.__actual.getdato().calcularsueldo()))
                bandera=not bandera
            else:
                self.__actual=self.__actual.getsiguiente()
                self.__indice+=1
        if bandera:
            print ("No se encontro empleado con dni ingresado")
        self.__actual=self.__comienzo
        self.__indice=0
    def toJSON(self):
        d=dict(__class__=self.__class__.__name__, Personal=[persona.toJSON() for persona in self])
        return d
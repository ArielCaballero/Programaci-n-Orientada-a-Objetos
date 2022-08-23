import Nodo
import Miinterface
from zope.interface import implementer

from Aparato import Aparato

@implementer(Miinterface.Interfaceejemplo)
class Lista:
    __comienzo=None
    __actual=None
    __index=0
    __tope=0
    def __init__(self):
        self.__comienzo=None
        self.__actual=None
        self.__index=0
        self.__tope=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.__index==self.__tope:
            self.__actual=self.__comienzo
            self.__index=0
            raise StopIteration
        else:
            self.__index+=1
            dato=self.__actual.getAparato()
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
        self.__index=0
        if posicion == 0:
            self.AgregarElemento(elemento)
        else:
            while (self.__index!=posicion and self.__actual!=None):
                ant=self.__actual
                self.__actual=self.__actual.getsiguiente()
                self.__index+=1
            if self.__index==posicion:
                nuevonodo=Nodo.Nodo(elemento)
                nuevonodo.setsiguiente(self.__actual)
                ant.setsiguiente(nuevonodo)
                self.__tope+=1
                self.__index=0
                self.__actual=self.__comienzo
            else:
                raise IndexError
        
    def MostrarElemento(self, posicion):
        self.__actual=self.__comienzo
        self.__index=0
        while (self.__index!=posicion and self.__index<self.__tope):
            self.__actual=self.__actual.getsiguiente()
            self.__index+=1
        if self.__index<self.__tope:
            print(type(self.__actual.getAparato()))
        else:
            raise IndexError
    def toJSON(self):
        d=dict(__class__=self.__class__.__name__, aparatos=[aparat.toJSON() for aparat in self])
        return d
from dataclasses import asdict
import Carrera

class Facultad:
    __codigo=0
    __nombre=""
    __direccion=""
    __localidad=""
    __telefono=""
    __carreras=[]
    def __init__(self, codigo, nombre, direccion, localidad, telefono, carreras):
        if (type(codigo)==int and type(nombre)==str and type(direccion)==str and type(localidad)==str and type(telefono)==str):
            self.__codigo=codigo
            self.__nombre=nombre
            self.__direccion=direccion
            self.__localidad=localidad
            self.__telefono=telefono
            self.__carreras=[]
            for carrera in carreras:
                auxiliar=Carrera.Carrera(int(carrera[1]),carrera[2],carrera[3],carrera[4],carrera[5])
                self.__carreras.append(auxiliar)
        else:
            print("Erroe en el tipo de datos")
    def getcodigo(self):
        return(self.__codigo)
    def getnombre(self):
        return(self.__nombre)
    def mostrarporcodigo(self, codigo):
        bandera=False
        if (self.getcodigo()==codigo):
            bandera= not bandera
            print("Lista de carreras de la {}:".format(self.getnombre()))
            for carrera in self.__carreras:
                print ("Nombre: {}     Duracion:{}".format(carrera.getnombre(), carrera.getduracion()))
        return bandera
    def getlocalidad(self):
        return(self.__localidad)
    def mostrarpornombre(self, nombre):
        bandera=False
        if (type(nombre)==str):
            i=0
            while(i<len(self.__carreras) and self.__carreras[i].getnombre()!=nombre):
                i=i+1
            if (i<len(self.__carreras)):
                bandera= not bandera
                print("Codigo:{}.{}    Facultad:{}    Localidad:{}".format(self.getcodigo(), self.__carreras[i].getcodigo(), self.getnombre(), self.getlocalidad()))
        else:
            print("Nombre debe ser una cadena")
        return bandera



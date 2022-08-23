import Facultad

class Manejafacultades:
    __listafacultades=[]
    def __init__(self):
        self.__listafacultades=[]
    def Agregarfacultad(self, facultad):
        if type(facultad)==Facultad.Facultad:
            self.__listafacultades.append(facultad)
    def buscarpornombre(self, nombre):
        bandera=False
        i=0
        while (i<len(self.__listafacultades) and bandera==False):
            if (self.__listafacultades[i].mostrarpornombre(nombre)):
                bandera=not bandera
            i+=1
        if (bandera==False):
            print("No se encontro la carrera por el nombre")
    def buscarporcarrera(self, codigo):
        bandera=False
        i=0
        while (bandera==False and i<len(self.__listafacultades)):
            if (self.__listafacultades[i].mostrarporcodigo(codigo)):
                bandera=not bandera
            i+=1
        if (bandera ==False):
            print("No se encontro la facultad por el codigo")
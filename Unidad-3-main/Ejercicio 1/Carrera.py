class Carrera:
    __codigo=0
    __nombre=""
    __fechainicio=""
    __duracion=""
    __titulo=""
    def __init__(self, codigo, nombre, fecha, duracion, titulo):
        if(type(codigo)==int and type(nombre)==str and type(fecha)== str and type(duracion)==str and type(titulo)==str):
            self.__codigo=codigo
            self.__nombre=nombre
            self.__fechainicio=fecha
            self.__duracion=duracion
            self.__titulo=titulo
        else:
            print("Error en tipos de datos en carga de carrera")
    def getnombre(self):
        return(self.__nombre)
    def getcodigo(self):
        return(self.__codigo)
    def getduracion(self):
        return(self.__duracion)
class jugador:
    __nombre=""
    __dni=""
    __ciudad=""
    __pais=""
    __fecha=""
    def __init__(self, nombre, dni, ciudad, pais, fecha):
        if (type(nombre)==str and type(dni)==str and type(ciudad)==str and type(pais)==str and type(fecha)==str):
            self.__nombre=nombre
            self.__dni=dni
            self.__ciudad=ciudad
            self.__pais=pais
            self.__fecha=fecha
        else:
            print("Error en carga jugador")
    def getdni(self):
        return self.__dni
    def __str__(self):
        return("Nombre: {}    DNI:{}   Fecha Nacimiento:{}\nCiudad: {}    Pais: {}".format(self.__nombre, self.__dni, self.__fecha, self.__ciudad, self.__pais))
    def getnombre (self):
        return self.__nombre
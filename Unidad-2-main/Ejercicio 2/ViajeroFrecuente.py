class ViajeroFrecuente:
    __num_viajero= 0
    __dni = ""
    __nombre= ""
    __apellido=""
    __millas_acum= 0
    def __init__(self, num, dni, nom, ap, mil=0):
        if (type(num)==int)&(type(dni)==int)&(type(nom)==str)&(type(ap)==str)&(type(mil)==int):
            self.__num_viajero=num
            self.__dni=dni
            self.__nombre=nom
            self.__apellido=ap
            self.__millas_acum=mil
        else:
            print("Error al cargar datos de viajero \n")
    def __str__(self):
        "{},{},{},{},{}".format(self.__num_viajero, self.__dni, self.__nombre, self.__apellido, self.__millas_acum)
    def CantidadTotalMillas(self):
        return(self.__millas_acum)
    def AcumularMillas(self, mill):
        if (type(mill)==int):
            self.__millas_acum=self.__millas_acum+mill
            return (self.__millas_acum)
        else:
            print("Error al ingresar cantidad de millas a acumular \n")
    def CanjearMillas(self, mill):
        if(type(mill)==int):
            if (self.__millas_acum>=mill):
                self.__millas_acum=self.__millas_acum-mill
            else:
                print("Cantidad de millas no es suficiente\n")
            return (self.__millas_acum)
        else:
            print("Error al ingresar cantidad de millas al canjear")
    def getnumerodeviajero(self):
        return (self.__num_viajero)

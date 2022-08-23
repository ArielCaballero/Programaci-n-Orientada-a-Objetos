class Ventana:
    __titulo=""
    __xsupizq=0
    __ysupizq=0
    __xinfder=0
    __yinfder=0
    def __init__(self, Titulo, Xsupizq=0, Ysupizq=0, Xinfder=500, Yinfder=500):
        if(type(Titulo)==str and type(Xsupizq)==int and type(Ysupizq)==int and type(Xinfder)==int and type(Yinfder)==int):
            if (Xinfder>Xsupizq and Yinfder>Xsupizq):    
                self.__titulo=Titulo
                self.__ysupizq=Ysupizq
                self.__yinfder=Yinfder
                self.__xinfder=Xinfder
                self.__xsupizq=Xsupizq
            else:
                print("Error: No es posible crear la ventana")
        else:
            print("Error al ingresar los datos")
    def mostrar(self):
        print("Esquina Superior Izquierda: ({},{})\nEsquina Inferior Derecha: ({},{})\n".format(self.__xsupizq,self.__ysupizq, self.__xinfder, self.__yinfder))
    def getTitulo(self):
        return(self.__titulo)
    def alto(self):
        return(self.__yinfder-self.__ysupizq)
    def ancho(self):
        return(self.__xinfder-self.__xsupizq)
    def moverDerecha(self, cantidad=1):
        if (self.__xinfder<=500-cantidad):
            self.__xinfder+=cantidad
        if (self.__xsupizq<=500-cantidad):
            self.__xsupizq+=cantidad
    def moverIzquierda(self, cantidad=1):
        if (self.__xinfder>=cantidad):
            self.__xinfder-=cantidad
        if (self.__xsupizq>=cantidad):
            self.__xsupizq-=cantidad
    def subir(self, cantidad=1):
        if (self.__xinfder>=500-cantidad):
            self.__yinfder-=cantidad
        if (self.__xsupizq>=cantidad):
            self.__ysupizq-=cantidad
    def bajar(self, cantidad=1):
        if (self.__xinfder<=500-cantidad):
            self.__yinfder+=cantidad
        if (self.__xsupizq<=500-cantidad):
            self.__ysupizq+=cantidad
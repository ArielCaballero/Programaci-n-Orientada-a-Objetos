import jugador

class manejadorjugadores:
    __Lista=[]
    def __init__(self):
        self.__Lista=[]
    def agregarjugador(self, jugado):
        if type(jugado)==jugador.jugador:
            self.__Lista.append(jugado)
        else:
            print("Error en tipo de dato al agregar jugador")
    def buscarjugador(self, nombre):
        valor=None
        i=0
        band=True
        while (i<len(self.__Lista) and band ):
            if self.__Lista[i].getnombre()==nombre:
                band=not band
                valor=self.__Lista[i]
            i+=1
        return valor
from ViajeroFrecuente import ViajeroFrecuente


class manejadorviajeros:
    def __init__(self):
        self.__Lista=[]
    def Cargarviajero(self, viajero):
        if (type(viajero)==ViajeroFrecuente):
            self.__Lista.append(viajero)
        else:
            print ("Tipo de dato incorrecto en carga de viajeros")
    def buscarviajero(self, numero):
        viajero=None
        for i in self.__Lista:
            if (i.getnumerodeviajero()==numero):
                viajero=i
        return(viajero)
    def test(self):
        viajero1=ViajeroFrecuente(10, 3333333, "Miguel", "Punto", 50)
        viajero2=ViajeroFrecuente(11, 4333333, "Valentin", "Correa", 100)
        viajero3=ViajeroFrecuente(12, 5333333, "Lisandro", "Cabrera", 150)
        self.Cargarviajero(viajero1)
        self.Cargarviajero(viajero2)
        self.Cargarviajero(viajero3)
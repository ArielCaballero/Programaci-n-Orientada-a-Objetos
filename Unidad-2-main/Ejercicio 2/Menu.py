class menu:
    __switch=None
    def __init__(self):
        self.__switch= {
            '1': self.opcion1,
            '2': self.opcion2,
            '3': self.opcion3,
            '0': self.salir
        }
    def opcion(self,op,viajero):
        func=self.__switch.get(op, lambda: print("Opción invalida"))
        if op=='1' or op=='2' or op=='3':
            func(viajero)
        else:
            func()
    def salir(self):
        print('Fin del programa')
    def opcion1(self, viajero):
        print("Millas: {}".format(viajero.CantidadTotalMillas()))    
    def opcion2(self, viajero):
        millas=int(input("Ingrese millas a acumular\n"))
        print("Millas totales: {}".format(viajero.AcumularMillas(millas)))
    def opcion3(self, viajero):
        millas=int(input("Ingrese millas a canjear\n"))
        print("Millas acumuladas que quedaron: {}".format(viajero.CanjearMillas(millas)))
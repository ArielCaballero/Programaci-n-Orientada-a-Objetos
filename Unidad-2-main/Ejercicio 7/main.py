import ViajeroFrecuente

if __name__=="__main__":
    Viajero1=ViajeroFrecuente.ViajeroFrecuente(1, 4214124, 'Juan', 'Perez', 150)
    Viajero2=ViajeroFrecuente.ViajeroFrecuente(2, 4213333, 'Jose', 'Alvarez', 300)
    print ("Millas iniciales del viajero {}: {}\n".format(Viajero1, Viajero1.CantidadTotalMillas()))
    numero=300
    print ("{} acumulo {} millas\nmillas actuales: {}\n".format(Viajero1, numero, numero+Viajero1))
    numero=50
    print ("{} canjeo {} millas\nmillas actuales: {}\n".format(Viajero1, numero, numero-Viajero1))
    print("\nCOMPARACION\n")
    numeroaigualar=400
    for i in range(3):
        if (Viajero1==numeroaigualar):
            print ("{} Tiene {} millas acumuladas\n".format(Viajero1, numeroaigualar))
            numero=100
            print ("{} acumulo {} millas\nmillas actuales: {}\n".format(Viajero1, numero, numero+Viajero1))
        else:
            print ("{} no tiene {} millas acumuladas\n".format(Viajero1, numeroaigualar))
            numero=200
            print ("{} canjeo {} millas\nmillas actuales: {}\n".format(Viajero1, numero, numero-Viajero1))
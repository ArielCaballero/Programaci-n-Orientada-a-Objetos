from ViajeroFrecuente import ViajeroFrecuente


import ViajeroFrecuente

if __name__=="__main__":
    Viajero1=ViajeroFrecuente.ViajeroFrecuente(1, 4214124, 'Juan', 'Perez', 150)
    Viajero2=ViajeroFrecuente.ViajeroFrecuente(2, 4213333, 'Jose', 'Alvarez', 300)
    print ("Millas iniciales viajero 1: {}\n".format(Viajero1.CantidadTotalMillas()))
    numero=250
    print ("El viajero 1 acumulo {} \nmillas actuales: {}\n".format(numero, Viajero1+numero))
    numero=50
    print ("El viajero 1 canjeo {} \nmillas actuales: {}\n".format(numero, Viajero1-numero))
    print("\nCOMPARACION\n")
    for i in range(2):
        if (Viajero1>Viajero2):
            print ("El viajero con datos:\n\n{}\nTiene mas millas".format(str(Viajero1)))
            numero=200
            print ("El viajero 1 canjeo {} \nmillas actuales: {}\n".format(numero, Viajero1-numero))
        else:
            print ("El viajero con datos:\n{}\nTiene mas millas o ambos tienen la misma cantidad de millas".format(str(Viajero2)))
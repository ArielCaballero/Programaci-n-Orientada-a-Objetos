import csv
import Menu
from ManejadorViajeros import manejadorviajeros
import ViajeroFrecuente

if __name__=="__main__":
    lista=manejadorviajeros()
    archivo=open("viajeros.csv")
    reader=csv.reader(archivo, delimiter=",")
    for fila in reader:
        lista.Cargarviajero(ViajeroFrecuente.ViajeroFrecuente(int(fila[0]), int(fila[1]), fila[2], fila[3], int(fila[4])))
    numviajero=int(input("Ingrese un numero de viajero\n"))
    viajero=lista.buscarviajero(numviajero)
    if (viajero!=None):
        menuviajero=Menu.menu()
        eleccion="-1"
        while (eleccion!="0"):
            eleccion=input("---------Menu---------\nSeleccione una opcion:\n1: Consultar Millas\n2: Acumular Millas\n3: Canjear Millas\n0: Salir\n\n")
            menuviajero.opcion(eleccion, viajero)
    else:
        print("No se encontro al viajero\n")
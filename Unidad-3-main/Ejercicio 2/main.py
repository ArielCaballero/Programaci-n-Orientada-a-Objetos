import csv

import flor
import ramo
import Manejadorflores
import Manejadorramos
import Menu

if __name__=="__main__":
    archivo=open('flores.csv')
    reader=csv.reader(archivo, delimiter=",")
    listaflores=Manejadorflores.manejadorflores()
    for fila in reader:
        auxiliar=flor.flor(fila[0], fila[1], fila[2], int(fila[3]))
        listaflores.Agregarflor(auxiliar)
    #listaflores.ordenar()
    listaramos=Manejadorramos.manejadorramos()
    menu=Menu.menu()
    control=input("Ingrese una opcion:\n1_Registrar ramo\n2_Mostrar 5 flores mas vendidas\n3_Mostrar flores vendidas en un tamaño\n0_Salir\n")
    while(control!="0"):
        menu.getopcion(control, listaramos, listaflores)
        control=input("Ingrese una opcion:\n1_Registrar ramo\n2_Mostrar 5 flores mas vendidas\n3_Mostrar flores vendidas en un tamaño\n0_Salir\n")
    archivo.close()
import csv

import Menu
from PlanAhorro import PlanAhorro
from ListaPlanes import ListaPlanes

if __name__=="__main__":
    Lista=ListaPlanes()
    archivo=open("planes.csv")
    reader=csv.reader(archivo, delimiter=";")
    for fila in reader:
        auxiliar=PlanAhorro(int(fila[0]),fila[1],fila[2],float(fila[3]))
        Lista.AgregarPlan(auxiliar)

    menuplanes=Menu.Menu()
    control="-1"
    while control!="0":
        control=input("--------Menu------\nSelecciones una opcion:\n1-Actualizar Valores\n2: Mostrar planes con valores menores\n3: Mostrar el monto a pagar para licitar un vehiculo\n4- Modificar las cuotas que debe tener licitas para pagar\n0- Salir\n")
        menuplanes.opcion(control, Lista)
import csv
import Registro
import ListaRegistros
import Menu

if __name__=="__main__":
    Lista=ListaRegistros.ListaRegistros()
    archivo=open("temperaturas.csv")
    reader=csv.reader(archivo, delimiter=",")
    for fila in reader:
        registrotemporal=Registro.Registro(float(fila[2]), int(fila[3]), float(fila[4]))
        Lista.AgregarRegistro(registrotemporal, int(fila[0]), int(fila[1]))
    
    control="-1"
    menureg=Menu.menu()
    while control!="0":
        control=input("--------Menu------\nSelecciones una opcion:\n1-Mostrar para cada variable el mayor y menor valor\n2: Temperatura Promedio\n3:Listar por dia\n0- Salir\n")
        menureg.opcion(control, Lista)
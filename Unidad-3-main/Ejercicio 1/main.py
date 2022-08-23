import Menu
import Manejafacultades
import Facultad
import csv

if __name__=="__main__":
    archivofacultad=open("Facultades.csv")
    reader=csv.reader(archivofacultad, delimiter=",")
    Listafacultades=Manejafacultades.Manejafacultades()
    bandera=True
    listaaux=[]
    for fila in reader:
        if (bandera):
            facultad=fila
            bandera= not bandera
        else:
            if(fila[0]==facultad[0]):
                listaaux.append(fila)
            else:
                Facultadaux=Facultad.Facultad(int(facultad[0]),facultad[1],facultad[2],facultad[3],facultad[4], listaaux)
                Listafacultades.Agregarfacultad(Facultadaux)
                listaaux.clear()
                facultad=fila
    Facultadaux=Facultad.Facultad(int(facultad[0]),facultad[1],facultad[2],facultad[3],facultad[4], listaaux)
    Listafacultades.Agregarfacultad(Facultadaux)
    listaaux.clear()
    menu=Menu.menu()
    control=input("\n--------Menu--------\nIngrese una opcion:\n1_ Buscar una carrera por su nombre\n2_ Buscar una carrera por su codigo\n0_ Salir\n")
    while (control!="0"):
        menu.getopcion(control, Listafacultades)
        control=input("\n--------Menu--------\nIngrese una opcion:\n1_ Buscar una carrera por su nombre\n2_ Buscar una carrera por su codigo\n0_ Salir\n")
    archivofacultad.close()
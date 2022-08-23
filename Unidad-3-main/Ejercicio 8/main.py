import json

import Lista
import ObjectEncoder
import Menu

if __name__=="__main__":
    jsonF=ObjectEncoder.ObjectEncoder()
    lista=Lista.Lista()
    diccionario=jsonF.leerJSONArchivo("Personal.json")
    lista=jsonF.decodificarDiccionario(diccionario)
    menu=Menu.Menu()
    control=input("Ingrese una opcion:\n1_Insertar un agente.\n2_Agregar un agente.\n3_Mostrar tipo de agente en una posicion.\n4_Generar listado de docentes investigadores.\n5_Cantidad de investigadores y docentes investigadores en un área.\n6_Listado con nombre apellido y tipo de agente ordenado.\n7_ Listar docentes investigadores de una categoria.\n8_ Guardar datos\n9_ Ingresar como Tesorero\n10_ Ingresar como Director\n0_Salir.\n")
    while(control!="0"):
        menu.getop(control, lista)
        control=input("Ingrese una opcion:\n1_Insertar un agente.\n2_Agregar un agente.\n3_Mostrar tipo de agente en una posicion.\n4_Generar listado de docentes investigadores.\n5_Cantidad de investigadores y docentes investigadores en un área.\n6_Listado con nombre apellido y tipo de agente ordenado.\n7_ Listar docentes investigadores de una categoria.\n8_ Guardar datos\n9_ Ingresar como Tesorero\n10_ Ingresar como Director\n0_Salir.\n")
    
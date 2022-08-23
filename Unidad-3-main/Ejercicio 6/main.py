from Menu import Menu
import ObjectEncoder
import Lista

if __name__=="__main__":
    lista=Lista.Lista()
    jsonF=ObjectEncoder.ObjectEncoder()
    diccionario=jsonF.leerJSONArchivo("aparatos.json")
    lista=jsonF.decodificarDiccionario(diccionario)
    menu=Menu()
    opcion=input("Ingrese una opción:\n1_Insertar Aparato\n2_Agregar Aparato\n3_Mostrar tipo de objeto dada una posicion\n4_ Mostrar Cantidad de aparatos marca philips\n5_Mostrar marca de todos los lavarropas con carga superior\n6_Mostrar datos de Aparatos\n7_Guardar datos\n0_Salir\n")
    while (opcion!='0'):
        menu.getop(opcion, lista)
        opcion=input("Ingrese una opción:\n1_Insertar Aparato\n2_Agregar Aparato\n3_Mostrar tipo de objeto dada una posicion\n4_ Mostrar Cantidad de aparatos marca philips\n5_Mostrar marca de todos los lavarropas con carga superior\n6_Mostrar datos de Aparatos\n7_Guardar datos\n0_Salir\n")
    
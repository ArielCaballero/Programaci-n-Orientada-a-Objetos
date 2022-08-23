import MENU
import Conjunto

if __name__=="__main__":
    menu=MENU.menu()
    conjunto_1=Conjunto.Conjunto()
    conjunto_2=Conjunto.Conjunto()
    control=input("\nIngrese una opcion:\n1_ Cargar conjunto 1\n2_ Cargar Conjunto 2\n3_ Union de Conjuntos\n4_ Diferencia de Conjuntos\n5_ Igualdad de Conjuntos\n6_ Vaciar Conjuntos\n0_ Salir\n\n")
    while (control!='0'):
        print(menu.getop(control, conjunto_1, conjunto_2))
        control=input("\nIngrese una opcion:\n1_ Cargar conjunto 1\n2_ Cargar Conjunto 2\n3_ Union de Conjuntos\n4_ Diferencia de Conjuntos\n5_ Igualdad de Conjuntos\n6_ Vaciar conjuntos\n0_ Salir\n\n")


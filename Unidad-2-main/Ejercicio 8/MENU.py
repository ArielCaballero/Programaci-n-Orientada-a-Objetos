from Conjunto import Conjunto

class menu:
    __switcher=None
    def __init__(self):
        self.__switcher={
            '1': self.opcion1,
            '2': self.opcion2,
            '3': self.opcion3,
            '4': self.opcion4,
            '5': self.opcion5,
            '6': self.opcion6,
            '99': self.opcion99,
            '0': self.salir
        }
    def getop(self, opcion, conjunto1, conjunto2):
        funcion=self.__switcher.get(opcion, lambda:print("Opcion inválida"))
        if (opcion=='5' or opcion=='4' or opcion=='3' or opcion=='99' or opcion=='6'):
            return(funcion(conjunto1, conjunto2))
        elif opcion=='1':
            return(funcion(conjunto1))
        elif opcion=='2':
            return(funcion(conjunto2))
        else:
            return(funcion())
    def opcion3(self, conjunto1, conjunto2):
        print("Union de Conjunto 1 y Conjunto 2")
        return(conjunto1+conjunto2)
    def opcion4 (self, conjunto1, conjunto2):
        print("Diferencia entre Conjunto 1 y Conjunto 2")
        return(conjunto1-conjunto2)
    def opcion5(self, conjunto1, conjunto2):
        resultado=None
        if (conjunto1==conjunto2):
            resultado="Ambos conjuntos son iguales"
        else:
            resultado="Los conjuntos son distintos"
        return(resultado)
    def salir(self):
        return("Usted salio del programa")
    def opcion1 (self, conjunto1):
        control=""
        while (control==""):
            numero=int(input("Ingrese un numero\n"))
            conjunto1.Agregarelemento(numero)
            control=input("Presione enter para continuar, cualquier tecla para salir de la carga del Conjunto1\n")
        return("Carga completada")
    def opcion2 (self, conjunto2):
        control=""
        while (control==""):
            numero=int(input("Ingrese un numero\n"))
            conjunto2.Agregarelemento(numero)
            control=input("Presione enter para continuar, cualquier tecla para salir de la carga del Conjunto2\n")
        return("Carga completada")
    def opcion99(self, conjunto1, conjunto2):
        conjunto1.test1()
        conjunto2.test2()
        return("Carga completada")
    def opcion6(self, conjunto1, conjunto2):
        conjunto1.clear()
        conjunto2.clear()
        return("Se vaciaron los conjuntos")
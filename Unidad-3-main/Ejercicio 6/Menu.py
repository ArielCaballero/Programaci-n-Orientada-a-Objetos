import json
import ObjectEncoder

from Aparato import Aparato
import Lista
import Televisor
import Heladera
import Lavarropas

class Menu:
    __switch=None
    def __init__(self):
        self.__switch={
            '1':self.opcion1,
            '2':self.opcion2,
            '3':self.opcion3,
            '4':self.opcion4,
            '5':self.opcion5,
            '6':self.opcion6,
            '7':self.opcion7,
            '0':self.salir
        }
    def getop(self, opcion, lista):
        funcion=self.__switch.get(opcion, lambda:print("Opcion inválida"))
        if (opcion=='1' or opcion=='2' or opcion=='3' or opcion=='4' or opcion=='5' or opcion=='6' or opcion=='7'):
            funcion(lista)
        else:
            funcion()

    def crearelemento(self):
        op=input("Ingrese un aparato\n1_ Televisor\n2_ Heladera\n3_Lavarropas\n")
        marca=input("Ingrese marca del aparato\n")
        modelo=input("Ingrese modelo del aparato\n")
        color=input("Ingrese color del aparato\n")
        pais=input("Ingrese pais del aparato\n")
        precio=float(input("Ingrese precio del aparato\n"))
        bandera=True
        while(bandera):
            if (op=='1'):
                tipo=input("Ingrese tipo del televisor\n")
                pulgadas=input("Ingrese pulgadas del televisor\n")
                definicion=input("Ingrese definicion del televisor\n")
                conexion=input("Ingrese conexion del televisor (si o no)\n")
                if (conexion!="No"):
                    conexion=True
                else:
                    conexion=False
                elemento=Televisor.Televisor(marca, modelo, color, pais, precio, tipo, pulgadas, definicion, conexion)
                bandera=False
            elif (op=='2'):
                capacidad=input("Ingrese capacidad de la heladera\n")
                freezer=input("Ingrese True si posee freezer (si o no)\n")
                ciclica=input("Ingrese True si es Ciclica (si o no)\n")
                if (ciclica=="si"):
                    ciclica=True
                else:
                    ciclica=False
                if (freezer=="si"):
                    freezer=True
                else:
                    freezer=False
                elemento=Heladera.Heladera(marca, modelo, color, pais, precio, capacidad, freezer, ciclica)
                bandera=False
            elif (op=='3'):
                capacidad=int(input("Ingrese la capacidad del Lavarropas en kg\n"))
                velocidad=input("Ingrese la velocidad del Lavarropas\n")
                cantidad=input("Ingrese la cantidad del Lavarropas\n")
                carga=input("Ingrese la carga del Lavarropas\n")
                elemento=Lavarropas.Lavarropas(marca, modelo, color, pais, precio, capacidad, velocidad, cantidad, carga)
                bandera=False
            else:
                print("Opcion no válida")
                op=input("Ingrese un aparato\n1_ Televisor\n2_ Heladera\n3_Lavarropas\n")
        return(elemento)
    
    def opcion1(self, lista):
        elemento=self.crearelemento()
        bandera=True
        while (bandera):
            try:
                posicion=int(input("Ingrese una posicion \n"))
                lista.InsertarElemento(elemento, posicion-1)
                bandera= not bandera
            except IndexError:
                print("Error: Indice inválido")
            
    def opcion2 (self, lista):
        elemento=self.crearelemento()
        lista.AgregarElemento(elemento)
    def opcion3(self,lista):
        bandera=True
        while (bandera):
            try:
                posicion=int(input("Ingrese una posicion \n"))
                lista.MostrarElemento(posicion-1)
                bandera= not bandera
            except IndexError:
                print("Error: Indice inválido")

    def opcion4(self, lista):
        cont=0
        for aparato in lista:
            if aparato.getmarca()=="philips":
                cont+=1
        print("El numero de aparatos marca philips es: {}".format(cont))
    def opcion5 (self, lista):
        for aparato in lista:
            if type(aparato)==Lavarropas.Lavarropas and aparato.getcarga()=="superior":
                print(aparato)
    def opcion6 (self,lista):
        for aparato in lista:
            aparato.calcularimporte()
            print("Aparato:{}    {}".format(str(type(aparato)), aparato))
    def opcion7 (self, lista):
        jsonF=ObjectEncoder.ObjectEncoder()
        d=lista.toJSON()
        jsonF.guardarJSONArchivo(d,"Aparatos.json")
    def salir(self):
        print("Usted salio del programa")

class Conjunto:
    def __init__(self):
        self.__Numeros=[]
    def Agregarelemento(self, numero):
        if (type(numero)==int): 
            i=0
            while (i<len(self.__Numeros) and (numero>self.__Numeros[i])):
                i+=1
            if i<len(self.__Numeros) and numero==self.__Numeros[i]:
                print ("Numero repetido")
            else:
                self.__Numeros.insert(i, numero)
    def __str__(self):
        return("{}".format(self.__Numeros))
    def test1(self):
        self.Agregarelemento(1)
        self.Agregarelemento(3)
        self.Agregarelemento(5)
        self.Agregarelemento(4)
        self.Agregarelemento(6)
        self.Agregarelemento(8)
    def test2(self):
        self.Agregarelemento(9)
        self.Agregarelemento(10)
        self.Agregarelemento(-5)
        self.Agregarelemento(1)
        self.Agregarelemento(0)
        self.Agregarelemento(3)
    def __add__(self, otro):
        resultado=None
        if type(otro)==type(self):
            Union=Conjunto()
            i=0
            j=0
            while (i<len(self.__Numeros) and j<len(otro.__Numeros)):
                if(self.__Numeros[i]>otro.__Numeros[j]):
                    Union.Agregarelemento(otro.__Numeros[j])
                    j+=1
                elif (self.__Numeros[i]<otro.__Numeros[j]):
                    Union.Agregarelemento(self.__Numeros[i])
                    i+=1
                else:
                    Union.Agregarelemento(self.__Numeros[i])
                    i+=1
                    j+=1
            while i<len(self.__Numeros):
                Union.Agregarelemento(self.__Numeros[i])
                i+=1
            while (j<len(otro.__Numeros)):
                Union.Agregarelemento(otro.__Numeros[j])
                j+=1
            resultado=Union
        else:
            print("Tipo de dato no valido")
        return(resultado)
    def __sub__(self, otro):
        resultado=None
        if type(otro)==type(self):
            Interseccion=Conjunto()
            i=0
            j=0
            while (i<len(self.__Numeros) and j<len(otro.__Numeros)):
                if(self.__Numeros[i]>otro.__Numeros[j]):
                    j+=1
                elif (self.__Numeros[i]<otro.__Numeros[j]):
                    Interseccion.Agregarelemento(self.__Numeros[i])
                    i+=1
                else:
                    i+=1
                    j+=1
            resultado=Interseccion
        else:
            print("Tipo de dato no valido")
        return(resultado)
    def __eq__(self, otro):
        bandera=False
        if (len(self.__Numeros)==len(otro.__Numeros)):
            bandera=True
            i=0
            while (i<len(otro.__Numeros) and (bandera==True)):
                j=0
                while (j<len(otro.__Numeros) and (self.__Numeros[i]!=otro.__Numeros[j])):
                    j+=1
                if j>=len(otro.__Numeros):
                    bandera=False
                i+=1
        return(bandera)
    def clear(self):
        self.__Numeros.clear()    
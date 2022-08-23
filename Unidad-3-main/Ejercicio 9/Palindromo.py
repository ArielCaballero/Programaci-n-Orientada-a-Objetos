class Palindromo:
    __palabra = None
    def __init__(self, palabra):
        self.__palabra = palabra
    def esPalindromo(self):
        i=0
        j=-len(self.palabra)
        bandera = True
        while i<abs(j) and bandera:
           if self.__palabra[i] != self.__palabra[i]:
               bandera=False
           else:
               i += 1
               j += 1
        return bandera
    def setPalabra(self, nuevaPalabra):
        self.__palabra = nuevaPalabra
    def nuevoesPalindromo(self):
        bandera=True
        if (len(self.__palabra)!=0):
            i=0
            j=len(self.__palabra)-1
            while i<=j and bandera:
               if self.__palabra[i] != self.__palabra[j]:
                   bandera=False
               i+=1
               j-=1
        else:
            bandera=False
        return bandera
class PlanAhorro:
    __codigo=0
    __modelo=""
    __version=""
    __valor=0
    cuotastotales=60
    cuotasnecesarias=10

    def __init__(self, Codigo, Modelo, Version, Valor):
        if ((type(Codigo)==int) and (type(Modelo)==str) and (type(Version)==str) and (type(Valor)==float)):
            self.__codigo= Codigo
            self.__modelo= Modelo
            self.__version= Version
            self.__valor= Valor
        else: 
            print("Error en la carga")
    def __str__(self):
        return("Codigo del Plan: {}\nModelo: {}\nVersion: {}\n".format(self.__codigo, self.__modelo, self.__version))
    def getvalor(self):
        return(self.__valor)
    def getcodigo(self):
        return(self.__codigo)
    def setvalor(self, nuevo):
        self.__valor=nuevo
    @classmethod
    def getcuotasnecesarias(cls):
        return(cls.cuotasnecesarias)
    @classmethod    
    def getcuotastotales(cls):
        return(cls.cuotastotales)
    @classmethod
    def setcuotasnecesarias(cls, valor):
        cls.cuotasnecesarias=valor
    @classmethod
    def setcuotastotales(cls, valor):
        cls.cuotastotales=valor

class Registro:
    def __init__(self, Temperatura=0.0, Humedad=0, Presion=0.0):
        if (type(Temperatura)==float)and(type(Humedad)==int)and(type(Presion)==float):
            self.__temperatura=Temperatura
            self.__humedad= Humedad
            self.__presion= Presion
    def gettemperatura(self):
        return(self.__temperatura)
    def gethumedad(self):
        return(self.__humedad)
    def getpresion(self):
        return(self.__presion)
    def __str__(self):
        return ("{:11}  {:7}  {:7}".format(self.__temperatura,self.__humedad,self.__presion))

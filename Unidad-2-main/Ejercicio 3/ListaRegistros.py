import Registro

class ListaRegistros:
    __Registros=[]
    def __init__(self):
        Auxiliar=Registro.Registro()
        for i in range(30):
            lis=[]
            for j in range(24):
                lis.append(Auxiliar)
            self.__Registros.append(lis)
    def AgregarRegistro(self, registro, dia, hora):
        if (type(registro)==Registro.Registro)and(type(dia)==int)and (type(hora)==int):
            self.__Registros[dia-1][hora]=registro
    def MostrarDatospordia(self, dia):
        print("Hora  Temperatura  Humedad  Presion  \n")
        for hora in range(24):
            print("{}  {}\n".format(hora, self.__Registros[dia][hora]))
    def MayorTemperatura(self):
        menor=self.__Registros[0][0].gettemperatura()
        for dia in range(len(self.__Registros)):
            for hora in range(len(self.__Registros[dia])):
                if (menor<=self.__Registros[dia][hora].gettemperatura()):
                    menor=self.__Registros[dia][hora].gettemperatura()
        return (menor)
    def MayorHumedad(self):
        menor=self.__Registros[0][0].gethumedad()
        for dia in range(len(self.__Registros)):
            for hora in range(len(self.__Registros[dia])):
                if (menor<=self.__Registros[dia][hora].gethumedad()):
                    menor=self.__Registros[dia][hora].gethumedad()
        return (menor)
    def MayorPresion(self):
        menor=self.__Registros[0][0].getpresion()
        for dia in range(len(self.__Registros)):
            for hora in range(len(self.__Registros[dia])):
                if (menor<=self.__Registros[dia][hora].getpresion()):
                    menor=self.__Registros[dia][hora].getpresion()
        return (menor)
    def MenorPresion(self):
        mayor=self.__Registros[0][0].getpresion()
        for dia in range(len(self.__Registros)):
            for hora in range(len(self.__Registros[dia])):
                if (mayor>=self.__Registros[dia][hora].getpresion()):
                    mayor=self.__Registros[dia][hora].getpresion()
        return (mayor)
    def MenorHumedad(self):
        mayor=self.__Registros[0][0].gethumedad()
        for dia in range(len(self.__Registros)):
            for hora in range(len(self.__Registros[dia])):
                if (mayor>=self.__Registros[dia][hora].gethumedad()):
                    mayor=self.__Registros[dia][hora].gethumedad()
        return (mayor)
    def MenorTemperatura(self):
        mayor=self.__Registros[0][0].gettemperatura()
        for dia in range(len(self.__Registros)):
            for hora in range(len(self.__Registros[dia])):
                if (mayor>=self.__Registros[dia][hora].gettemperatura()):
                    mayor=self.__Registros[dia][hora].gettemperatura()
        return (mayor)
    def Promedioporhora(self, hora):
        contador=0
        sumador=0
        for i in range(len(self.__Registros)):
            sumador+=self.__Registros[i][hora].gettemperatura()
            contador+=1
        return (sumador/contador)
    def PromedioMensual(self):
        print ("Promedios Mensuales de Temperaura por hora\n")
        for hora in range(len(self.__Registros[1])):
            print("{}: {}".format(hora, self.Promedioporhora(hora)))
    def test(self):
        reg1=Registro.Registro(1,0,25.8,50,250.5)
        reg2=Registro.Registro(1,1,26,51,260)
        reg3=Registro.Registro(1,2,27,49,220)
        reg4=Registro.Registro(1,3,25,34,512)
        self.__Registros.append(reg1)
        self.__Registros.append(reg2)
        self.__Registros.append(reg3)
        self.__Registros.append(reg4)
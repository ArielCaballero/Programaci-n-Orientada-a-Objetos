class menu:
    def __init__(self):
        self.__switch={
            "1": self.opcion1,
            "2": self.opcion2,
            "3": self.opcion3,
            "0": self.salir
        }
    def opcion(self, op, Listadereg):
        func=self.__switch.get(op, lambda:print("Opcion invalida"))
        if (op=="1" or op=="2" or op=="3"):
            func(Listadereg)
        else:
            func()
    def opcion1(self, Listadereg):
        print("Mayor Temperatura: {}\n Menor Temperatura: {}\n Mayor Humedad: {}\n Menor Humedad: {}\n Mayor Presion {}\n Menor Presion {}\n".format(Listadereg.MayorTemperatura(),Listadereg.MenorTemperatura(),Listadereg.MayorHumedad(), Listadereg.MenorHumedad(), Listadereg.MayorPresion(), Listadereg.MenorPresion()))
    def opcion2(self, Listadereg):
        Listadereg.PromedioMensual()
    def opcion3(self, Listadereg):
        dia=int(input("Ingrese un dia\n"))
        Listadereg.MostrarDatospordia(dia-1)
    def salir(self):
        print("Fin del programa")
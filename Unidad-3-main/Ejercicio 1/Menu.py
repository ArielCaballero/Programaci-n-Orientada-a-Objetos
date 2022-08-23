class menu:
    __switch=""
    def __init__(self):
        self.__switch={
            '1': self.opcion1,
            '2': self.opcion2,
            '0': self.salir
        }
    def getopcion(self, opcion, manejador):
        funcion=self.__switch.get(opcion, lambda:print("Opcion no valida"))
        if (opcion=='1' or opcion=='2'):
            funcion(manejador)
        else:
            funcion()
    def salir(self):
        return("Ha salido del menu")
    def opcion1(self, manejador):
        nombre=input("Ingrese un nombre de carrera\n")
        manejador.buscarpornombre(nombre)
    def opcion2(self, manejador):
        bandera=True
        while (bandera):
            try:
                codigo=int(input("Ingrese un codigo de facultad\n"))
                bandera=not bandera
            except ValueError:
                print("Invalido")
        manejador.buscarporcarrera(codigo)
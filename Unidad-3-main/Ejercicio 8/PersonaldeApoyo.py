import Personal

class PersonaldeApoyo(Personal.Personal):
    __categoria=""
    def __init__(self, cuil, apellido, nombre, sueldobasico, antiguedad, categoria):
        if type(categoria)==int:
            super().__init__(cuil, apellido, nombre, sueldobasico, antiguedad)
            self.__categoria=categoria
            self.__porcentaje=1
            if self.__categoria<=10:
                self.__porcentaje=1.1
            elif self.__categoria>10 and self.__categoria<=20:
                self.__porcentaje=1.2
            elif self.__categoria>=21 and self.__categoria<=22:
                self.__porcentaje=1.3
        else:
            print("Error en creacion de Personal de Apoyo")
    def calcularsueldo(self):
        return super().calcularsueldo()*self.__porcentaje
    def modificarporcentaje(self, nuevoporcentaje):
        self.__porcentaje=nuevoporcentaje
    def __str__(self):
        return (super().__str__()+" Personal de Apoyo")
    def toJSON(self):
        d=dict(
            __class__=self.__class__.__name__, 
            __atributos__=dict(
                cuil=self.getcuil(),
                apellido=self.getapellido(),
                nombre=self.getnombre(),
                sueldobasico=self.getsueldobasico(),
                antiguedad=self.getantiguedad(),
                categoria=self.__categoria
        ))
        return d
        
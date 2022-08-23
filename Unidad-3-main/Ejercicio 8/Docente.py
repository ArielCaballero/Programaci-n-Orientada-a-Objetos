import Personal

class Docente(Personal.Personal):
    __carrera=""
    __cargo=""
    __catedra=""
    __porcentaje=0
    def __init__(self, cuil, apellido, nombre, sueldobasico, antiguedad, area, tipo, carrera, cargo, catedra):
        super().__init__(cuil, apellido, nombre, sueldobasico, antiguedad, area, tipo, carrera, cargo, catedra)
        self.__carrera=carrera
        self.__cargo=cargo
        self.__catedra=catedra
        self.__porcentaje=1
        if self.__cargo=="Simple":
            self.__porcentaje=1.1
        elif self.__cargo=="Semiexclusivo":
            self.__porcentaje=1.2
        elif self.__cargo=="Exclusivo":
            self.__porcentaje=1.5
    def getcarrera(self):
        return self.__carrera
    def getcargo(self):
        return self.__cargo
    def modificarporcentaje(self, nuevoporcentaje):
        self.__porcentaje=nuevoporcentaje
    def getcatedra(self):
        return self.__catedra
    def __str__(self):
        return (super().__str__()+" Docente")
    def calcularsueldo(self):
        return super().calcularsueldo()*self.__porcentaje
    def toJSON(self):
        d=dict(
            __class__=self.__class__.__name__, 
            __atributos__=dict(
               cuil=self.getcuil(),
                apellido=self.getapellido(),
                nombre=self.getnombre(),
                sueldobasico=self.getsueldobasico(),
                antiguedad=self.getantiguedad(),
                area="",
                tipo="",
                carrera=self.__carrera,
                cargo=self.__cargo,
                catedra=self.__catedra
        ))
        return d
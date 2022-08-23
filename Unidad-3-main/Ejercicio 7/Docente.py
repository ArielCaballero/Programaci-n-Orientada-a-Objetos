import Personal

class Docente(Personal.Personal):
    __carrera=""
    __cargo=""
    __catedra=""
    def __init__(self, cuil, apellido, nombre, sueldobasico, antiguedad, area, tipo, carrera, cargo, catedra):
        super().__init__(cuil, apellido, nombre, sueldobasico, antiguedad, area, tipo, carrera, cargo, catedra)
        self.__carrera=carrera
        self.__cargo=cargo
        self.__catedra=catedra
    def getcarrera(self):
        return self.__carrera
    def getcargo(self):
        return self.__cargo
    def getcatedra(self):
        return self.__catedra
    def __str__(self):
        return (super().__str__()+" Docente")
    def calcularsueldo(self):
        valor=super().calcularsueldo()
        if self.__cargo=="Simple":
            valor=valor*1.1
        elif self.__cargo=="Semiexclusivo":
            valor=valor*1.2
        elif self.__cargo=="Exclusivo":
            valor=valor*1.5
        return valor
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
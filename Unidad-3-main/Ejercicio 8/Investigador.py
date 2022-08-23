from Personal import Personal

class Investigador(Personal):
    __area=""
    __tipo=""
    def __init__(self, cuil, apellido, nombre, sueldobasico, antiguedad, area, tipo, carrera, cargo, catedra):
        super().__init__(cuil, apellido, nombre, sueldobasico, antiguedad, area, tipo, carrera, cargo, catedra)
        self.__area=area
        self.__tipo=tipo
    def calcularsueldo(self):
        return super().calcularsueldo()
    def getarea(self):
        return self.__area
    def gettipo(self):
        return self.__tipo
    def __str__(self):
        return (super().__str__()+" Investigador")
    def toJSON(self):
        d=dict(
            __class__=self.__class__.__name__, 
            __atributos__=dict(
                cuil=self.getcuil(),
                apellido=self.getapellido(),
                nombre=self.getnombre(),
                sueldobasico=self.getsueldobasico(),
                antiguedad=self.getantiguedad(),
                area=self.__area,
                tipo=self.__tipo,
                carrera="",
                cargo="",
                catedra=""
        ))
        return d
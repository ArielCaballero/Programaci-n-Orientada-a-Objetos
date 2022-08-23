import Investigador
import Docente

class DocenteInvestigador(Docente.Docente, Investigador.Investigador):
    __categoria=""
    __importeextra=""
    def __init__(self, cuil, apellido, nombre, sueldobasico, antiguedad,categoria, importeextra, area, tipo, carrera, cargo, catedra):
        super().__init__(cuil, apellido, nombre, sueldobasico, antiguedad, area, tipo, carrera, cargo, catedra)
        self.__categoria=categoria
        self.__importeextra=importeextra
    def getcategoria(self):
        return(self.__categoria)
    def getimporte(self):
        return self.__importeextra
    def calcularsueldo(self):
        return super().calcularsueldo()+self.__importeextra
    def modificarImporteExtra(self, nuevoimporteextra):
        self.__importeextra=nuevoimporteextra
    def __str__(self):
        return (super().__str__())
    def toJSON(self):
        d=dict(
            __class__=self.__class__.__name__, 
            __atributos__=dict(
                cuil=self.getcuil(),
                apellido=self.getapellido(),
                nombre=self.getnombre(),
                sueldobasico=self.getsueldobasico(),
                antiguedad=self.getantiguedad(),
                categoria=self.__categoria,
                importeextra=self.__importeextra,
                area=self.getarea(),
                tipo=self.gettipo(),
                carrera=self.getcarrera(),
                cargo=self.getcargo(),
                catedra=self.getcatedra()
        ))
        return d
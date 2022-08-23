import numpy as np
import Cama
from ManejadorMedicamentos import ManejadorMedicamentos

class ManejadorCamas:
    def __init__(self):
        camavacia=Cama.cama()
        self.__ArregloCamas=np.full(30, camavacia)
    def AgregarCama(self, camaagregada, id):
        if (type(camaagregada)==Cama.cama and type(id)==int):
            self.__ArregloCamas[id-1]=camaagregada
    def test(self):
        camausada=Cama.cama(200, "True", "Juan", "Esclerosis", "07/12/2002", "")
        self.__ArregloCamas[29]=camausada
    def Buscaridcama(self, camaabuscar):
        valor=None
        if type(camaabuscar)==Cama.cama:
            i=0
            while (self.__ArregloCamas[i]!=camaabuscar and i<len(self.__ArregloCamas)):
                i=i+1
            if(i<len(self.__ArregloCamas)):
                valor=i
        return (valor)
    def BuscarporNombre(self, nombre):
        valorderetorno=None
        i=0
        while ((i<len(self.__ArregloCamas) and (self.__ArregloCamas[i].getpaciente()!=nombre))):
            i=i+1
        if (i<len(self.__ArregloCamas)):
            valorderetorno=self.__ArregloCamas[i]
        return(valorderetorno)
    def DarAlta (self, nombre):
        if (type(nombre)==str):
            camabuscada=self.BuscarporNombre(nombre)
            if (camabuscada!=None):
                camabuscada.setfechaalta()
                idcamabuscada=self.Buscaridcama(camabuscada)
                Medicamentos=ManejadorMedicamentos.Buscarporcama(idcamabuscada)
                print("\n\nPaciente: {}    Cama: {}    Habitacion: {}\nDiagnostico: {}        Fecha de Internacion: {}\nFecha de Alta: {}\n".format(camabuscada.getpaciente(), idcamabuscada, camabuscada.gethabitacion(), camabuscada.getdiagnostico(), camabuscada.getfechainternacion(), camabuscada.getfechaalta()))
                total=0 
                print("Medicamento/Monodroga          Presentacion        Cantidad        Precio")
                for medicam in Medicamentos:
                    print("{:10}/{:21}{:20}{:3}{:19}".format(medicam.getNombremedicamento(), medicam.getmonodroga(),medicam.getpresentacion(), medicam.getcantidad(), medicam.getprecio()))
                    total+=medicam.getprecio()
                print("\nTotal: {:67}".format(total))
            else:
                print("No se encontro al Paciente")
    def buscarpordiagnostico(self, diagnostico):
        if (type(diagnostico)==str):
            for cama in self.__ArregloCamas:
                if diagnostico==cama.getdiagnostico():
                    print ("Datos:\n {}".format(cama))
        else:
            print("Error en el tipo de dato")

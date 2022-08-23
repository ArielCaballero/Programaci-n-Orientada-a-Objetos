import Medicamentos

class ManejadorMedicamentos:
    __ListaMedicamentos=[]
    @classmethod
    def AgregarMedicamento(cls, medicamento):
        if(type(medicamento)==Medicamentos.Medicamento):
            cls.__ListaMedicamentos.append(medicamento)
    @classmethod
    def Buscarporcama(cls, idcama):
        Lista=[]
        for i in range(len(cls.__ListaMedicamentos)):
            if (cls.__ListaMedicamentos[i].getidcama()==idcama+1):
                Lista.append(cls.__ListaMedicamentos[i])
        return (Lista)
import csv
import ManejadorCamas
import ManejadorMedicamentos
import Cama
import Medicamentos

if __name__=="__main__":
    archivocamas=open("camas.csv")
    archivomedicamentos=open("medicamentos.csv")
    readercamas=csv.reader(archivocamas, delimiter=";")
    readermedicamentos=csv.reader(archivomedicamentos, delimiter=";")
    Arreglocamas=ManejadorCamas.ManejadorCamas()
    Arreglocamas.test()
    bandera=True
    for fila in readercamas:
        if bandera==True:
            bandera=not bandera
        else:
            auxiliar=Cama.cama(int(fila[1]), fila[2], fila[3], fila[4], fila[5], fila[6])
            Arreglocamas.AgregarCama(auxiliar, int(fila[0]))
    bandera=True
    for fila in readermedicamentos:
        if bandera==True:
            bandera=not bandera
        else:
            auxiliar=Medicamentos.Medicamento(int(fila[0]), int(fila[1]), fila[2], fila[3], fila[4], int(fila[5]), float(fila[6]))
            ManejadorMedicamentos.ManejadorMedicamentos.AgregarMedicamento(auxiliar)
    nombre=input("Ingrese el nombre de un paciente a dar de alta\n")
    Arreglocamas.DarAlta(nombre)
    diagnos=input("Ingrese un diagnostico\n")
    Arreglocamas.buscarpordiagnostico(diagnos)
    archivocamas.close()
    archivomedicamentos.close()

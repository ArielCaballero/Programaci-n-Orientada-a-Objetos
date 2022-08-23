import csv

import Manejadorcontratos
import Manejadorequipos
import Manejadorjugadores
import contrato
import equipo
import jugador

if __name__=="__main__":
    archivoequipos=open("equipos.csv")
    readerequipos=csv.reader(archivoequipos, delimiter=";")
    band=True
    for fila in readerequipos:
        if band:
            listaequipos=Manejadorequipos.manejadorequipos(int(fila[0]))
            band=not band
        else:
            auxiliar=equipo.equipo(fila[0], fila[1])
            listaequipos.agregarequipo(auxiliar)
    archivoequipos.close()
    archivojugadores=open("jugadores.csv")
    readerjugadores=csv.reader(archivojugadores, delimiter=";")
    listajugadores=Manejadorjugadores.manejadorjugadores()
    for fila in readerjugadores:
        auxiliar=jugador.jugador(fila[0], fila[1], fila[2], fila[3], fila[4])
        listajugadores.agregarjugador(auxiliar)
    archivojugadores.close()
    listacontratos=Manejadorcontratos.manejadorcontratos()
    control=input("Ingrese cualquier tecla para definir un contrato, s para salir\n")
    while control !="s":
        equip=input("Ingrese nombre de equipo\n")
        jugad=input("Ingrese nombre de jugador\n")
        fechainicio=input("Ingrese fecha de inicio de contrato (dd/mm/aaaa)\n")
        fechafin=input("Ingrese fecha de fin de contrato (dd/mm/aaaa)\n")
        pago=float(input("Ingrese el pago mensual\n"))
        listacontratos.agregarcontrato(listaequipos.buscarequipo(equip).firmarcontrato(listajugadores.buscarjugador(jugad), fechainicio, fechafin, pago))
        control=input("Ingrese cualquier tecla para definir un contrato, s para salir\n")
    listacontratos.agregarcontrato(listaequipos.buscarequipo("Boca").firmarcontrato(listajugadores.buscarjugador("Julian Alvarez"), "15/05/2020", "16/7/2022", 15000.00))
    listacontratos.agregarcontrato(listaequipos.buscarequipo("Boca").firmarcontrato(listajugadores.buscarjugador("Juan Quintas"), "15/12/2021", "16/06/2022", 17000.00))
    dniabuscar=input("Ingrese un dni para buscar jugador\n")
    listacontratos.mostrarjugadorpordni(dniabuscar)
    identificador=int(input("Ingrese el identificador de un equipo\n"))
    listaequipos.vencimientosequipo(identificador)
    nombreequipo=input("Ingrese el nombre de un equipo\n")
    listaequipos.calcularimportes(nombreequipo)
    
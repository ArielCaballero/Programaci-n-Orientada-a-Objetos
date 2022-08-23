import ramo
import Manejadorflores
import flor

class manejadorramos:
    __lista=[]
    def __init__(self):
        self.__lista=[]
    def Agregarramo(self, ramos):
        if type(ramos)==ramo.ramo:
            self.__lista.append(ramos)
        else:
            print("Error en manejador ramos en carga")
    def mostrarfloresmasvendidas(self, manejadorflores):
        lista=[]
        for i in range(manejadorflores.getcantidad()):
            listaaux=[]
            aux=0
            for ramos in self.__lista:
                aux+=ramos.buscarflores(manejadorflores.getflor(i).getnumero())
            listaaux.append(aux)
            listaaux.append("{} {}".format(manejadorflores.getflor(i).getnombre(), manejadorflores.getflor(i).getcolor()))
            lista.append(listaaux)
        lista.sort(reverse=True)
        print("Los nombres de las flores mas vendidas son:")
        i=0
        while i<len(lista) and i<5:
            if lista[i][0]>0:
                print(lista[i][1])
            i+=1
    def mostrarflorentamano(self, tamano, manejadorflores):
        Lista=[]
        for i in range(manejadorflores.getcantidad()):
            j=0
            bandera=False
            while (j<len(self.__lista) and bandera==False):
                if (self.__lista[j].gettamano()==tamano and self.__lista[j].encontrarflor(manejadorflores.getflor(i).getnumero())):
                    bandera=not bandera
                j+=1
            if bandera:
                Lista.append(manejadorflores.getflor(i).getnombre()+" "+manejadorflores.getflor(i).getcolor())
        print("Las flores en los ramos de tamaño {}:".format(tamano))
        for flor in Lista:
            print(flor)
class Medicamento:
    __idCama=0
    __idMedicamento=0
    __NombreComercial=""
    __monodroga=""
    __presentacion=""
    __cantidadaplicada=""
    __precio=""
    def __init__(self, idc, idm, nombre, monodroga, presentacion, cantidad, precio):
        if ((type(idc)==int)and (type(idm)==int)and (type(nombre)==str)and (type(monodroga)==str)and (type(presentacion)==str)and(type(cantidad)==int)and (type(precio)==float)):
            if(idc>0 and idc<=30):   
                if(idm>0 and idm<=100):    
                    self.__idCama=idc
                    self.__idMedicamento=idm
                    self.__NombreComercial=nombre
                    self.__monodroga=monodroga
                    self.__presentacion=presentacion
                    self.__cantidadaplicada=cantidad
                    self.__precio=precio
                else:
                    print("Identificador del medicamento no es valido")
            else:
                print("identificador de la cama no es valido")
        else:
            print("Datos no validos para medicamento")
    def getNombremedicamento (self):
        return(self.__NombreComercial)
    def getmonodroga(self):
        return(self.__monodroga)
    def getpresentacion(self):
        return(self.__presentacion)
    def getcantidad(self):
        return(self.__cantidadaplicada)
    def getprecio(self):
        return(self.__precio)
    def getidcama(self):
        return(self.__idCama)
    def __str__(self):
        return("id cama:{}\nid medicamento: {}\nNombre comercial: {}\nMonodroga: {}\nPresentacion: {}\nCantidad: {}\nPrecio: {}".format(self.__idCama, self.__idMedicamento,self.getNombremedicamento(),self.getmonodroga(),self.getpresentacion(),self.getcantidad(),self.getprecio()))
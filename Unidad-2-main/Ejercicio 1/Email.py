class email:
    def __init__(self, idc="", dom="", tipo="", cont="12345678"):
        if (type(idc)==str) &(type(dom)==str)& (type(tipo)==str)& (type(cont)==str):
            self.__idcuenta = idc
            self.__dominio = dom
            self.__tipodominio = tipo
            self.__contrasena= cont
        else:
            print("Parametros no validos")
    def retornaemail(self):
        return (self.__idcuenta.replace(" ", "") + "@" + self.__dominio.strip() + "." + self.__tipodominio.strip())
    def getdominio(self):
        return (self.__dominio)
    def getidc(self):
        return (self.__idcuenta)
    def crearcuenta(self, correo):
        if (type(correo)==str):
            lista=correo.split(sep='@')
            self.__idcuenta=(lista[0])
            self.__dominio=(lista[1].split(sep='.'))[0]
            self.__tipodominio=(lista[1].split(sep='.'))[1]
        else:
            print("error en crearcuenta \n")
    def cambircontrasena(self):
        contra=input("Ingrese contraseña actual \n")
        if (contra==self.__contrasena):
            contra=input("Ingrese nueva contraseña \n")
            self.__contrasena=contra
        else:
            print("Contraseña incorrecta \n")
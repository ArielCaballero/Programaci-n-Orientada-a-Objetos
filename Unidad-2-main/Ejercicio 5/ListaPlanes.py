from PlanAhorro import PlanAhorro

class ListaPlanes:
    def __init__(self):
        self.__Lista=[]
    def AgregarPlan(self, plan):
        if (type(plan)==PlanAhorro):
            self.__Lista.append(plan)
    def Actualizarplanes(self):
        for plan in self.__Lista:
            nuevo_valor=float(input(plan))
            plan.setvalor(nuevo_valor)
    def MostrarMenores(self, valor):
        for plan in self.__Lista:
            if (valor>(plan.getvalor())):
                print(plan)
    def MostrarMontos(self):
        print("Montos para licitar:\n")
        for plan in self.__Lista:
            monto=(((plan.getvalor()/PlanAhorro.getcuotastotales())+plan.getvalor()*0.1)*PlanAhorro.getcuotasnecesarias())
            print("Codigo: {}   Monto:{:2}".format(plan.getcodigo(), monto))

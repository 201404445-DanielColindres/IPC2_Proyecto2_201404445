from nodoLinea import nodoLinea
from nodoComponente import nodoComponente
from nodoEnsamble import nodoEnsamble

class entradas():
    def __init__(self):
        self.lineasEn = None
        self.tamañoLineas = 0
        self.componentesEn =  None
        self.tamañoComponentes = []
        self.instruccionesEn = None
        self.tamañoInstruciiones = []

    def agregarLinea(self, valor):
        #recibe la linea de produccion
        agregarL = nodoLinea(valor)
        if self.tamañoLineas == 0:
            self.lineasEn = agregarL
            self.tamañoLineas = 1
            #recibe sus compnetes---------------------------
            agregarC = nodoComponente(componente, tiempoComp)
            if self.tamañoComponentes == 0:
                self.lineasEn.componentes = agregarC
                self.tamañoComponentes = 1
            else:
                pass
            #recibe las instrucciones----------------------
            agregarI = nodoEnsamble(producto, instruccion)
            if self.tamañoInstruciiones == 0:
                self.lineasEn.instrucciones = agregarI
                self.tamañoInstruciiones = 1
            else:
                pass
        else:
            pass

    '''def agregarComponente(self,com, t):
        pass

    def agregarInstrucion(self, prod, inst):
        pass'''

    def configuracion(self):#carga del archivo de la configuracion
        pass

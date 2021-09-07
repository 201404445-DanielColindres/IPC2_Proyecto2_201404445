class nodoEnsamble:
    def __init__(self, producto, instruccion):
        self.producto = producto
        self.instruccion = instruccion
        self.siguiente = None
        self.anterior = None
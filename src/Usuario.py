class Usuario:
    # Contructor.
    def __init__(self, nombre, credito=None):
        self.__nombre=nombre
        self.credito=credito
        self.listaSubasta=list()

    # Getters.
    def getNombre(self):
        return self.__nombre
    def getCredito(self):
        return self.credito
    def getListaSubasta(self):
        return self.listaSubasta

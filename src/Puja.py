class Puja:
    #Constructor
    def __init__(self, usuario, credito):
        self.__usuario=usuario
        self.__credito=credito

    # Getters.
    def getUsuario(self):
        return self.__usuario
    def getCredito(self):
        return self.__credito
from src.Puja import Puja
from src.Usuario import Usuario


class Subasta:
    # Constructor.
    def __init__(self, producto, usuario):
        self.__producto=producto
        self.__usuario=usuario
        usuario.getListaSubasta().append(self)
        self.__estado=True
        self.__lista=list()
        self.__puja_mayor=Puja(Usuario("", 0), 0)

    # Getters & Setters.
    def getProducto(self):
        return self.__producto
    def setProducto(self, producto):
        self.__producto=producto

    def getUsuario(self):
        return self.__usuario
    def setUsuario(self, usuario):
        self.__usuario=usuario

    def getEstado(self):
        return self.__estado
    def setEstado(self, estado):
        self.__estado=estado

    def getLista(self):
        return self.__lista

    def getPujaMayor(self):
        return self.__puja_mayor

    def setPujaMayor(self, puja):
        self.__puja_mayor = puja

    # Metodo para que los distintos usuarios puedan pujar por el
    # objeto de la subasta.
    def pujar(self, Usuario, credito=None):
        if self.__estado:
            if not credito==None  and self.getEstado() and Usuario.getCredito()>self.getPujaMayor().getCredito() and credito> self.getPujaMayor().getCredito() and not Usuario==self.getUsuario():
                self.getLista().append(Puja(Usuario, credito))
                self.setPujaMayor(Puja(Usuario, credito))
                print("Puja realizada correctamente")
                Usuario.credito=Usuario.credito-credito;
                return True
            elif credito==None and self.__estado and not Usuario==self.getUsuario():
                self.__lista.append(Puja(Usuario, self.getPujaMayor().getCredito() + 1))
                self.setPujaMayor(Puja(Usuario, self.getPujaMayor().getCredito() + 1))
                print("Puja automatica realizada correctamente")
                Usuario.credito = Usuario.credito - 1;
                return True
            elif Usuario==self.getUsuario():
                print("La puja no puede realizarse por el dueño de la subasta")
                return False
            else:
                print("La puja no se pudo realizar")
                return False
        else:
            print("Subasta cerrada")

    #Metodo para cerrar una puja.
    def cerrarSubasta(self):
        self.__usuario.credito=self.__usuario.credito+self.getPujaMayor().getCredito()
        print("- Se cierra la subatsa de " + self.__usuario.getNombre())
        self.__estado=False;

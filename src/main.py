from src.Subasta import Subasta
from src.Usuario import Usuario

t = Usuario("Toni", 100)
p = Usuario("Pere", 150)
e = Usuario("Enric", 300)
st = Subasta("SmartPhone", t)
st.pujar(p, 100)
print("Puja mayor actual, Nombre: " + st.getPujaMayor().getUsuario().getNombre() + ", credito: " + str(st.getPujaMayor().getCredito()))
st.pujar(e, 50)
print("Puja mayor actual, Nombre: " + st.getPujaMayor().getUsuario().getNombre() + ", credito: " + str(st.getPujaMayor().getCredito()))
st.cerrarSubasta()
st.pujar(e, 200)

# print(t.getNombre())
# print(t.getCredito())
# print(p.getNombre())
# print(p.getCredito())
# print(e.getNombre())
# print(e.getCredito())
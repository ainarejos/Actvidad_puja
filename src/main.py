from src.Subasta import Subasta
from src.Usuario import Usuario
# Se crean los usuarios.
t = Usuario("Toni", 100)
p = Usuario("Pere", 150)
e = Usuario("Enric", 300)
# Toni crea una subasta de un smartphone.
st = Subasta("SmartPhone", t)
print("- Pere puja por la subasta de toni con 100€")
st.pujar(p, 100)
print("--------------------------------------")
print("- Se muestra la puja mayor actual de la subasta de toni")
print("Puja mayor actual, Nombre: " + st.getPujaMayor().getUsuario().getNombre() + ", credito: " + str(st.getPujaMayor().getCredito()))
print("--------------------------------------")
print("- Enric puja por la subasta de toni con 50€")
st.pujar(e, 50)
print("--------------------------------------")
print("- Se muestra la puja mayor actual de la subasta de toni")
print("Puja mayor actual, Nombre: " + st.getPujaMayor().getUsuario().getNombre() + ", credito: " + str(st.getPujaMayor().getCredito()))
print("--------------------------------------")
# Se cierra la subasta
st.cerrarSubasta()
print("--------------------------------------")
print("- Enric intenta apostar en la subasta de toni")
st.pujar(e, 200)
print("--------------------------------------")
# Pere crea una subasta de una impresora 3D
sp = Subasta("Impresora 3D", p)
print("- Enric realiza una puja automatica en la subasta de la impresora 3D")
sp.pujar(e)
print("--------------------------------------")
sp.cerrarSubasta()
print("--------------------------------------")
print("- Se listan los usuarios")
listaUsuarios=list();
listaUsuarios.append(t)
listaUsuarios.append(p)
listaUsuarios.append(e)
for x in listaUsuarios:
    print(x.getNombre() + ", " + str(x.getCredito()))
print("--------------------------------------")
print("- Se listan los usuarios con sus respectivas subastas")
for x in listaUsuarios:
    print(x.getNombre() + ":")
    for y in x.listaSubasta:
        print(y.getProducto())
print("--------------------------------------")
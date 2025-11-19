
lista_usuarios = []

def agregar(nombre, precio, cantidad):
        usuario = {}
        usuario['nombre'] = nombre
        usuario['precio'] = precio
        usuario['cantidad'] = cantidad
        
        return usuario
while True:
    nombre = input("ingrese usuario")
    precio = int(input("ingrese precio"))
    cantidad = int(input("ingrese la cantida"))

    nuevo_usuario = agregar(nombre, precio, cantidad)
    lista_usuarios.append(nuevo_usuario)
    print(lista_usuarios)
    continue
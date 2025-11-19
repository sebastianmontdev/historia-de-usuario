# Inicializamos una lista vacía que persistirá durante todo el programa.
# Es buena práctica usar un nombre que indique que contiene múltiples elementos, como 'lista_usuarios'
lista_usuarios = []

# Definimos la función fuera del bucle para que solo se cree una vez
def agregar(nombre, precio, cantidad):
    usuario = {}
    usuario['nombre'] = nombre
    usuario['precio'] = precio
    usuario['cantidad'] = cantidad
    return usuario

while True:    
    nombre = input("Ingrese nombre: ")
    precio = int(input("Ingrese precio: "))
    cantidad = int(input("Ingrese la cantidad: "))

    # Creamos el nuevo diccionario de usuario
    nuevo_usuario = agregar(nombre, precio, cantidad)
    
    # Agregamos el nuevo diccionario a la lista usando .append()
    lista_usuarios.append(nuevo_usuario)
    
    # Imprimimos la lista completa para verificar los datos guardados
    print("Datos guardados:", lista_usuarios)
    
    # Opcional: preguntar si se quiere agregar otro usuario o salir
    continuar = input("¿Desea agregar otro usuario? (s/n): ")
    if continuar.lower() != 's':
        break

print("Programa finalizado. Lista final de usuarios:", lista_usuarios)

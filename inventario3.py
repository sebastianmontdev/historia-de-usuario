#declaramos la lista inventario y le damos un contenido
inventario = [
     {"nombre" : "papa","precio" : 2.5, "cantidad" : 5},
     {"nombre" : "banano","precio" : 1.0, "cantidad" : 3}
     ]
#declaramos la fucion calcular
def calcular():
    total_inventario = 0
    for i in inventario:
        precio_total = i['precio'] * i['cantidad']
        total_inventario = total_inventario + precio_total
        cantidad = len(inventario)
    print(f"el total el dinero de todo el inventario es:", total_inventario, "la cantidad de productos es:", cantidad)
def mostrar():
        for item in inventario:
           print(f"Producto: {item['nombre']} | Precio: {item['precio']} | Cantidad: {item['cantidad']}")
def agregar(nombre, precio, cantidad):
        usuario = {}
        usuario['nombre'] = nombre
        usuario['precio'] = precio
        usuario['cantidad'] = cantidad
        
        return usuario

inicio = True
while inicio == True:
    print("1.Agregar producto")
    print("2. Mostrar inventario")
    print("3. buscar")
    print("4. actualizar")
    print("5. eliminar")
    print("6. estadisticas")
    print("7. guardar csv")
    print("8. cargar cvs")
    print("9. salir")
    opcion = int(input("ingrese una opcion"))
    if opcion == 1:
        while True:
            nombre = input("ingrese nombre")
            precio = float(input("ingrese precio"))
            cantidad = int(input("ingrese la cantida"))

            nuevo_usuario = agregar(nombre, precio, cantidad)
            inventario.append(nuevo_usuario)
            print(inventario)
            salir_registro = input("desea registrar otro producto?")
            if salir_registro == "si":
                 print("inicia proceso de registro")
                 continue
            else:
                break
    elif opcion == 2:
         mostrar()
    elif opcion == 3:
         print
    elif opcion == 4:
        print()
    elif opcion == 5:
        print()
    elif opcion == 6:
        calcular()
    elif opcion == 7:
        print()
    elif opcion == 8:
        print()
    elif opcion == 9:
        print("saliendo del sistema")
        break
    else:
         print("ingrese un dato correcto")
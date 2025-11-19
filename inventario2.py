inventario = [
     {"nombre" : "papa","precio" : 2.5, "cantidad" : 5},
     {"nombre" : "banano","precio" : 1.0, "cantidad" : 3}
     ]

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
    print("3. Calcular estadísticas")
    print("4. salir")
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
        for item in inventario:
            print(f"Producto: {item['nombre']} | Precio: {item['precio']} | Cantidad: {item['cantidad']}")
    elif opcion == 3:
        print()
    elif opcion == 4:
        inicio == False()




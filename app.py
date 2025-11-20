
from modulo_servicios import mostrar,agregar,calcular,buscar
inventario = [
     {"nombre" : "papa","precio" : 2.5, "cantidad" : 5},
     {"nombre" : "banano","precio" : 1.0, "cantidad" : 3}
     ]
#declaramos la fucion calcular


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
         mostrar(inventario)
    elif opcion == 3:
        nombre_buscado = input("Ingrese el nombre del producto que desea buscar: ").lower()
        buscar(inventario,nombre_buscado)
    elif opcion == 4:
        print()
    elif opcion == 5:
        print()
    elif opcion == 6:
        calcular(inventario)
    elif opcion == 7:
        print()
    elif opcion == 8:
        print()
    elif opcion == 9:
        print("saliendo del sistema")
        break
    else:
         print("ingrese un dato correcto")
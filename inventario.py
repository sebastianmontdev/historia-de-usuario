#creamos el bucle 
while True:
    #declaramos la variable nombre
    nombre = input("ingrese el nombre del producto")
    #ponemos un condicional para asegurarnos de que el dato sea texto
    #isalpha revisa si los datos son texto sin espacios ni careacteres especiales
    if nombre.isalpha():
        #todo funciono
        print("dato guardado")
    #else por si no se cumple la condicion
    else:
        #mensajes de error si no se cumple la condicion
        print("porfavor ingrese solo texto sin espacios")
    #abrimos un bucle para errores
    while True:
        #lo usamos para atrapar errores
        try:
            #declaramos la variable precio
            precio = float(input("ingrese el precio"))
            #todo funciono
            print("dato guardado")
            #para salir del bucle
            break 
        #si atrapa un erro mostra el mensaje
        except ValueError:
            print("ingrese un valor correcto")
            #abrimos un bucle para errores
    while True:
        #lo usamos para atrapar errores
        try:
            #declaramos la variable cantidad
            cantidad = int(input("ingrese la cantidad de ese producto"))
            #todo funciono
            print("dato guardado")
            #para salir del bucle
            break 
        #si atrapa un erro mostra el mensaje
        except ValueError:
            print("ingrese numeros enteros")
    #aqui guardamos el precio final
    costo_total = cantidad * precio
    #aqui mostramos la "factura"
    print(f"producto:{nombre} precio:{precio} total:{costo_total}")

#en general este sirve para poder guardar los datos de un producto y mostrar
#una especie de factura con los datos del producto y el precio final


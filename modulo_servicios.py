import csv
def calcular(inventario):
    total_inventario = 0
    unidades_totales = 0
    for i in inventario:
        unidades_totales = unidades_totales + i['cantidad']
        precio_total = i['precio'] * i['cantidad']
        total_inventario = total_inventario + precio_total
        cantidad = len(inventario)
        producto_mas_caro = max(inventario, key=lambda producto: producto['precio'])
        mayor_stock = max(inventario, key=lambda producto: producto['cantidad'])
    print(f"la cantidad de unidades que hay en el inventario es: ",unidades_totales)
    print(f"el total el dinero de todo el inventario es:", total_inventario)
    print(f"la cantidad de productos es:", cantidad)
    print(f"el producto mas caro de la lista es",producto_mas_caro)
    print(f"el producto con mayor stock es",mayor_stock)
def mostrar(inventario):
        for item in inventario:
           print(f"Producto: {item['nombre']} | Precio: {item['precio']} | Cantidad: {item['cantidad']}")
def agregar(nombre, precio, cantidad):
        usuario = {}
        usuario['nombre'] = nombre
        usuario['precio'] = precio
        usuario['cantidad'] = cantidad
        
        return usuario

def buscar(inventario,nombre_buscado):
    for producto in inventario:
        if producto["nombre"].lower() == nombre_buscado:
            print("\n✅ Producto encontrado:")
            print(f"   Nombre: {producto['nombre']}")
            return producto
        else:
            print("producto inexisten")

def guardar(inventario):
    encabezados = ['nombre', 'precio', 'cantidad']
    nombre_archivo_csv = 'archivo.csv'
    try:
        with open(nombre_archivo_csv, 'w', newline='', encoding='utf-8') as archivo_csv:
            writer = csv.DictWriter(archivo_csv, fieldnames=encabezados)
            writer.writeheader()
            writer.writerows(inventario)
            print(f"✅ ¡Datos guardados exitosamente en '{nombre_archivo_csv}'!")

    except IOError:
        print(f"❌ Error al intentar abrir o escribir en el archivo: {nombre_archivo_csv}")

def cargar(inventario):
    nombre_archivo = 'archivo.csv'
    try:
        with open(nombre_archivo, mode='r', encoding='utf-8') as archivo_csv:
            lector_diccionario = csv.DictReader(archivo_csv)
            for fila in lector_diccionario:
                if 'edad' in fila and fila['edad'].isdigit():
                    fila['edad'] = int(fila['edad'])
                inventario.append(fila)
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no fue encontrado.")
    except Exception as e:
        print(f"Ocurrió un error al leer el CSV: {e}")

def eliminar(inventario):
    nombre_a_eliminar = input("inserte el nombre del producto que desea eliminar")
    elemento_encontrado = None
    for producto in inventario:
        if producto["nombre"] == nombre_a_eliminar:
            elemento_encontrado = producto
            break
            if elemento_encontrado:
                inventario.remove(elemento_encontrado)
                print(f"✅ Diccionario con nombre '{nombre_a_eliminar}' eliminado.")
            else:
                print(f"❌ Diccionario con nombre '{nombre_a_eliminar}' no encontrado.")
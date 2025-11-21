def calcular(inventario):
    total_inventario = 0
    unidades_totales = 0
    for i in inventario:
        unidades_totales = unidades_totales + i['cantidad']
        precio_total = i['precio'] * i['cantidad']
        total_inventario = total_inventario + precio_total
        cantidad = len(inventario)
        producto_mas_caro = max(inventario, key=lambda producto: producto['precio'])
    print(producto_mas_caro)
    print(f"la cantidad de unidades que hay en el inventario es: ",unidades_totales)
    print(f"el total el dinero de todo el inventario es:", total_inventario)
    print(f"la cantidad de productos es:", cantidad)
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
             
              
          
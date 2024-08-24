inventario = [{"nombre":"McFlury", "precio":2.50, "stock":10}]

def menu_principal():
    """
    Muestra el menu principal
    """
    while True:
        print("Menu Principal")
        print("1. Agregar Producto")
        print("2. Mostrar Inventario")
        print("3. Vender Producto")
        print("4. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            mostrar_inventario()
        elif opcion == "3":
            vender_producto()
        elif opcion == "4":
            break
        else:
            print("Opcion no valida. Por favor intente de nuevo")
        
def agregar_producto():
    """
    Agregar un nuevo producto al inventario
    """

    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad del producto: "))

    producto = {"nombre": nombre, "precio": precio, "stock": cantidad}
    inventario.append(producto)

def mostrar_inventario():

    """
    Muestra todos los productos del inventario
    """

    if len(inventario) == 0:
        print("El inventario esta vacio")
    else:
        print("Presentando Inventario")
        for producto in inventario:
            print(f"Nombre:{producto['nombre']}, Precio: {producto['precio']:.2f}, Cantidad: {producto['stock']}")

def vender_producto():
    """
    Vende un producto, actualiza el inventario y muestra el total de la venta
    """
    
    nombre = input("Ingrese el nombre del producto que desea vender: ")

    for producto in inventario:
        if producto["nombre"].lower() == nombre.lower():
            cantidad = int(input(f"¿Cuantas unidadaes de {nombre} desea vender?: "))
            if cantidad <= producto["stock"]:
                producto["stock"] -= cantidad
                total = cantidad * producto["precio"]
                print(f"Venta realizada. Total: ${total:.2f}")

                if producto["stock"] == 0:
                    print(f"El producto {nombre} se ha agotado.")
                    reponer = input(f"¿Desea agregar más stock a {nombre}? si/no: ")
                    if reponer.lower() == "si":
                        cantidad_reponer = int(input(f"Ingrese la cantidad de stock a agregar a {nombre}: "))
                        producto["stock"] += cantidad_reponer
                        print(f"Stock de {nombre} actualizado. Nueva cantidad: {producto['stock']}")

                return
            else:
                print("No hay suficiente Stock en Inventario")
                return

    print("Producto no encontrado en el inventario")

menu_principal()
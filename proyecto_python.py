# Requisitos para la entrega:
# 1. Crear un menú interactivo
# Crear un menú interactivo utilizando bucles while y condicionales if-elif-else: 
#   El menú debe permitir al usuario seleccionar entre diferentes opciones relacionadas con la gestión de productos. 
#   Entre las opciones, deben incluirse: agregar productos al inventario y mostrar los productos registrados.
# 2. Agregar productos al inventario
# Implementar la funcionalidad para agregar productos a una lista: 
#   Cada producto debe ser almacenado en una lista, y debe tener al menos un nombre y una cantidad asociada.
# 3. Mostrar el inventario
# Mostrar los productos ingresados: 
#   Al seleccionar la opción correspondiente, el sistema debe permitir visualizar los productos almacenados hasta el momento.

# Lista para almacenar los productos del inventario (cada producto es una lista [nombre, cantidad])
inventario = []

def agregar_producto():
    """Función para agregar un producto al inventario."""
    nombre = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad del producto: "))
    # Agregar el producto a la lista como una lista interna [nombre, cantidad]
    inventario.append([nombre, cantidad])
    print(f"Producto '{nombre}' agregado con cantidad {cantidad}.")

def mostrar_inventario():
    """Función para mostrar el inventario de productos utilizando un bucle while."""
    if inventario:
        print("\nInventario de productos:")
        index = 0  # Índice para recorrer la lista de inventario
        while index < len(inventario):
            producto = inventario[index]
            print(f"Producto: {producto[0]}, Cantidad: {producto[1]}")
            index += 1  # Incrementar el índice para pasar al siguiente producto
    else:
        print("El inventario está vacío.")

def menu():
    """Función para mostrar el menú y gestionar la interacción con el usuario."""
    while True:
        print("\n----- Menú de Gestión de Inventario -----")
        print("1. Agregar un producto al inventario")
        print("2. Mostrar inventario")
        print("3. Salir")
        
        opcion = input("Seleccione una opción (1/2/3): ")
        
        if opcion == '1':
            agregar_producto()
        elif opcion == '2':
            mostrar_inventario()
        elif opcion == '3':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción entre 1 y 3.")


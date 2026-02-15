from servicios.inventario import Inventario
from modelo.producto import Producto
def mostrar_menu():
    """Muestra el menú principal de opciones"""
    print("\n" + "="*50)
    print("           SISTEMA DE GESTIÓN DE INVENTARIOS")
    print("="*50)
    print("1. Añadir producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto por nombre")
    print("5. Listar todos los productos")
    print("6. Salir")
    print("="*50)


def validar_entero(mensaje: str) -> int:
    """Valida y devuelve un número entero ingresado por el usuario"""
    while True:
        try:
            valor = input(mensaje)
            return int(valor)
        except ValueError:
            print("❌ Error: Debe ingresar un número entero válido.")


def validar_float(mensaje: str) -> float:
    """Valida y devuelve un número decimal ingresado por el usuario"""
    while True:
        try:
            valor = input(mensaje)
            return float(valor)
        except ValueError:
            print("❌ Error: Debe ingresar un número válido.")


def agregar_producto(inventario: Inventario):
    """Gestiona el proceso de añadir un nuevo producto"""
    print("\n--- AÑADIR NUEVO PRODUCTO ---")
    
    id_producto = validar_entero("ID del producto: ")
    
    # Verificar si el ID ya existe
    if inventario._buscar_por_id(id_producto) is not None:
        print("❌ Error: Ya existe un producto con ese ID.")
        return
    
    nombre = input("Nombre del producto: ").strip()
    if not nombre:
        print("❌ Error: El nombre no puede estar vacío.")
        return
    
    cantidad = validar_entero("Cantidad inicial: ")
    if cantidad < 0:
        print("❌ Error: La cantidad no puede ser negativa.")
        return
    
    precio = validar_float("Precio unitario: $")
    if precio < 0:
        print("❌ Error: El precio no puede ser negativo.")
        return
    
    producto = Producto(id_producto, nombre, cantidad, precio)
    
    if inventario.agregar_producto(producto):
        print("✅ Producto agregado exitosamente.")
    else:
        print("❌ Error: No se pudo agregar el producto.")


def eliminar_producto(inventario: Inventario):
    """Gestiona el proceso de eliminar un producto"""
    print("\n--- ELIMINAR PRODUCTO ---")
    
    if inventario.esta_vacio():
        print("⚠️  El inventario está vacío.")
        return
    
    id_producto = validar_entero("ID del producto a eliminar: ")
    
    if inventario.eliminar_producto(id_producto):
        print("✅ Producto eliminado exitosamente.")
    else:
        print("❌ Error: No se encontró un producto con ese ID.")


def actualizar_producto(inventario: Inventario):
    """Gestiona el proceso de actualizar un producto"""
    print("\n--- ACTUALIZAR PRODUCTO ---")
    
    if inventario.esta_vacio():
        print("⚠️  El inventario está vacío.")
        return
    
    id_producto = validar_entero("ID del producto a actualizar: ")
    
    if inventario._buscar_por_id(id_producto) is None:
        print("❌ Error: No se encontró un producto con ese ID.")
        return
    
    print("\n¿Qué desea actualizar?")
    print("1. Cantidad")
    print("2. Precio")
    print("3. Ambos")
    
    opcion = validar_entero("Seleccione una opción (1-3): ")
    
    nueva_cantidad = None
    nuevo_precio = None
    
    if opcion in [1, 3]:
        nueva_cantidad = validar_entero("Nueva cantidad: ")
        if nueva_cantidad < 0:
            print("❌ Error: La cantidad no puede ser negativa.")
            return
    
    if opcion in [2, 3]:
        nuevo_precio = validar_float("Nuevo precio: $")
        if nuevo_precio < 0:
            print("❌ Error: El precio no puede ser negativo.")
            return
    
    if inventario.actualizar_producto(id_producto, nueva_cantidad, nuevo_precio):
        print("✅ Producto actualizado exitosamente.")
    else:
        print("❌ Error: No se pudo actualizar el producto.")


def buscar_producto(inventario: Inventario):
    """Gestiona el proceso de búsqueda de productos por nombre"""
    print("\n--- BUSCAR PRODUCTO POR NOMBRE ---")
    
    if inventario.esta_vacio():
        print("⚠️  El inventario está vacío.")
        return
    
    nombre_busqueda = input("Ingrese nombre o parte del nombre a buscar: ").strip()
    
    if not nombre_busqueda:
        print("❌ Error: Debe ingresar un texto para buscar.")
        return
    
    resultados = inventario.buscar_por_nombre(nombre_busqueda)
    
    if resultados:
        print(f"\n✅ Se encontraron {len(resultados)} resultado(s):")
        print("-" * 50)
        for producto in resultados:
            print(producto)
        print("-" * 50)
    else:
        print("⚠️  No se encontraron productos con ese nombre.")


def listar_productos(inventario: Inventario):
    """Muestra todos los productos en el inventario"""
    print("\n--- LISTA DE PRODUCTOS EN INVENTARIO ---")
    
    productos = inventario.listar_productos()
    
    if not productos:
        print("⚠️  El inventario está vacío.")
        return
    
    print(f"\nTotal de productos: {len(productos)}")
    print("-" * 60)
    for producto in productos:
        print(producto)
    print("-" * 60)


def main():
    """Función principal que ejecuta el menú interactivo"""
    inventario = Inventario()
    
    while True:
        mostrar_menu()
        opcion = validar_entero("\nSeleccione una opción (1-6): ")
        
        if opcion == 1:
            agregar_producto(inventario)
        elif opcion == 2:
            eliminar_producto(inventario)
        elif opcion == 3:
            actualizar_producto(inventario)
        elif opcion == 4:
            buscar_producto(inventario)
        elif opcion == 5:
            listar_productos(inventario)
        elif opcion == 6:
            print("\n👋 ¡Gracias por usar el sistema de inventarios!")
            break
        else:
            print("❌ Opción inválida. Por favor seleccione una opción entre 1 y 6.")
        
        input("\nPresione ENTER para continuar...")


if __name__ == "__main__":
    main()
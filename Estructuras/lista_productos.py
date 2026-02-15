# LISTA DE INVENTARIO = ordenada + mutable + indexada
productos = ["Camisa", "Pantalon", "Zapatos"]
print("Inventario Inicial:", productos)

# Acceso por índice (0, 1, 2...)
# Supongamos que queremos ver el tercer producto
print("Producto en posicion 2:", productos[2])

# Modificar un producto (mutable)
# Cambiamos 'Pantalon' por 'Pantalon de Jean'
productos[1] = "Pantalon de Jean"
print("Inventario Modificado:", productos)

# Agregar un producto al final
# Útil para la función "Añadir producto" del sistema.
productos.append("Gorra")
print("Inventario con nuevo producto:", productos)

# Eliminar por valor
# Útil si el usuario quiere borrar un producto específico por nombre
productos.remove("Camisa")
print("Inventario tras eliminar 'Camisa':", productos)

# Eliminar por índice y recuperar el elemento
# El método pop() es útil para registrar cuál fue el último producto vendido o sacado
ultimo_sacado = productos.pop()
print("Producto vendido:", ultimo_sacado)
print("Lista de inventario final:", productos)
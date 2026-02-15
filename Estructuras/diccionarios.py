# DICCIONARIO = pares clave:valor + mutable + acceso por clave
# Ideal para representar un producto individual con sus propiedades
producto = {
    "id": "P001",
    "nombre": "Camiseta Deportiva",
    "precio": 19.99,
    "stock": 50
}

# Acceso por clave
print("Nombre del producto:", producto["nombre"])

# Agregar nuevo dato (Ej: Categoria)
producto["categoria"] = "Ropa"
print("Con categoria:", producto)

# Modificar dato (Ej: Actualizar stock tras una venta)
producto["stock"] = 45
print("Stock actualizado:", producto["stock"])

# Lectura segura con get (evita que el programa se cierre si la clave no existe)
print("Garantia:", producto.get("garantia", "No especificada"))

# Iterar por items (Para mostrar la ficha técnica del producto)
print("\n--- Ficha del Producto ---")
for clave, valor in producto.items():
    print(f"{clave.capitalize()}: {valor}")

# Eliminar una propiedad (Ej: eliminar precio de oferta)
producto.pop("id")
print("\nSin ID:", producto)
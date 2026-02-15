# SET = elementos únicos + sin orden + no indexado
# Ideal para manejar categorías de productos sin repeticiones
categorias_lista = ["Ropa", "Calzado", "Ropa", "Accesorios", "Calzado"]

# Crear un conjunto a partir de la lista para eliminar 
# El set() ayuda a mostrarle al usuario una lista limpia de qué categorías existen en la tienda sin repetir el producto.
categorias_unicas = set(categorias_lista)
print("Lista original (con duplicados):", categorias_lista)
print("Categorias únicas (SET):", categorias_unicas)

# Agregar un elemento nuevo
categorias_unicas.add("Deportes")
# Si intentas agregar uno que ya existe, no pasará nada
categorias_unicas.add("Ropa") 
print("Categorias tras intentar agregar 'Deportes' y 'Ropa':", categorias_unicas)

# Verificar existencia rápida (muy eficiente en conjuntos)
print("¿Existe la categoria 'Hogar'?", "Hogar" in categorias_unicas)

# Operaciones de conjuntos (Útil para comparar inventarios de dos sucursales)
sucursal_A = {"Camisa", "Pantalon", "Zapatos"}
sucursal_B = {"Zapatos", "Gorra", "Reloj"}

print("\n--- Comparación de Sucursales ---")
print("Productos en AMBAS sucursales (Intersección):", sucursal_A & sucursal_B)
print("Total de productos distintos (Unión):", sucursal_A | sucursal_B)
print("Productos solo en Sucursal A (Diferencia):", sucursal_A - sucursal_B)
# TUPLA = ordenada + inmutable (no se puede cambiar)
# Útil para datos constantes como la ubicación de la tienda o impuestos
ubicacion_tienda = (-2.1708, -79.9224)  # Latitud, Longitud (Guayaquil)

print("Ubicacion de la sucursal:", ubicacion_tienda)

# Acceso por índice
print("Latitud:", ubicacion_tienda[0])

# Intento de cambio (esto dará un error porque las tuplas son inmutables)
# ubicacion_tienda[0] = -2.1800  
print("Nota: Los datos de ubicacion estan protegidos y no pueden cambiarse.")

# Configuración de moneda y país que la tienda no cambiará
configuracion_fija = ("USD", "Ecuador", 0.15) # Moneda, País, IVA
print("Configuracion del sistema:", configuracion_fija)
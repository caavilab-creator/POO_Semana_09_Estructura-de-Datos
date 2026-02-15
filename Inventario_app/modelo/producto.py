class Producto:
    """
    Clase que representa un producto en el inventario.
    Encapsula los datos y comportamientos básicos de un producto.
    """
    
    def __init__(self, id_producto: int, nombre: str, cantidad: int, precio: float):
        """
        Constructor de la clase Producto.
        
        Args:
            id_producto: Identificador único del producto
            nombre: Nombre descriptivo del producto
            cantidad: Cantidad disponible en inventario
            precio: Precio unitario del producto
        """
        self._id = id_producto
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio
    
    # Getters
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def nombre(self) -> str:
        return self._nombre
    
    @property
    def cantidad(self) -> int:
        return self._cantidad
    
    @property
    def precio(self) -> float:
        return self._precio
    
    # Setters
    @nombre.setter
    def nombre(self, nuevo_nombre: str):
        if nuevo_nombre.strip():
            self._nombre = nuevo_nombre
        else:
            raise ValueError("El nombre no puede estar vacío")
    
    @cantidad.setter
    def cantidad(self, nueva_cantidad: int):
        if nueva_cantidad >= 0:
            self._cantidad = nueva_cantidad
        else:
            raise ValueError("La cantidad no puede ser negativa")
    
    @precio.setter
    def precio(self, nuevo_precio: float):
        if nuevo_precio >= 0:
            self._precio = nuevo_precio
        else:
            raise ValueError("El precio no puede ser negativo")
    
    def __str__(self) -> str:
        """Representación en cadena del producto para mostrar al usuario"""
        return f"ID: {self._id} | Nombre: {self._nombre} | Cantidad: {self._cantidad} | Precio: ${self._precio:.2f}"
    
    def to_dict(self) -> dict:
        """Convierte el objeto a diccionario para facilitar operaciones"""
        return {
            'id': self._id,
            'nombre': self._nombre,
            'cantidad': self._cantidad,
            'precio': self._precio
        }
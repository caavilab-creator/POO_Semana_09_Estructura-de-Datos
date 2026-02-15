from modelo.producto import Producto
from typing import List, Optional

class Inventario:
    """
    Clase que gestiona la colección de productos y sus operaciones.
    Implementa los principios de encapsulamiento y abstracción.
    """
    
    def __init__(self):
        """Inicializa el inventario con una lista vacía de productos"""
        self._productos: List[Producto] = []
    
    def agregar_producto(self, producto: Producto) -> bool:
        """
        Añade un nuevo producto al inventario si su ID es único.
        
        Args:
            producto: Instancia de Producto a agregar
            
        Returns:
            True si se agregó exitosamente, False si el ID ya existe
        """
        if self._buscar_por_id(producto.id) is not None:
            return False
        
        self._productos.append(producto)
        return True
    
    def eliminar_producto(self, id_producto: int) -> bool:
        """
        Elimina un producto del inventario por su ID.
        
        Args:
            id_producto: ID del producto a eliminar
            
        Returns:
            True si se eliminó exitosamente, False si no se encontró
        """
        producto = self._buscar_por_id(id_producto)
        if producto:
            self._productos.remove(producto)
            return True
        return False
    
    def actualizar_producto(self, id_producto: int, nueva_cantidad: int = None, nuevo_precio: float = None) -> bool:
        """
        Actualiza la cantidad y/o precio de un producto existente.
        
        Args:
            id_producto: ID del producto a actualizar
            nueva_cantidad: Nueva cantidad (opcional)
            nuevo_precio: Nuevo precio (opcional)
            
        Returns:
            True si se actualizó exitosamente, False si no se encontró el producto
        """
        producto = self._buscar_por_id(id_producto)
        if not producto:
            return False
        
        try:
            if nueva_cantidad is not None:
                producto.cantidad = nueva_cantidad
            if nuevo_precio is not None:
                producto.precio = nuevo_precio
            return True
        except ValueError:
            return False
    
    def buscar_por_nombre(self, nombre_busqueda: str) -> List[Producto]:
        """
        Busca productos cuyo nombre contenga la cadena de búsqueda (insensible a mayúsculas/minúsculas).
        
        Args:
            nombre_busqueda: Texto a buscar en los nombres de productos
            
        Returns:
            Lista de productos que coinciden con la búsqueda
        """
        nombre_busqueda = nombre_busqueda.lower().strip()
        return [p for p in self._productos if nombre_busqueda in p.nombre.lower()]
    
    def listar_productos(self) -> List[Producto]:
        """Devuelve una copia de la lista completa de productos"""
        return self._productos.copy()
    
    def _buscar_por_id(self, id_producto: int) -> Optional[Producto]:
        """
        Método privado para buscar un producto por su ID.
        
        Args:
            id_producto: ID a buscar
            
        Returns:
            Producto si se encuentra, None en caso contrario
        """
        for producto in self._productos:
            if producto.id == id_producto:
                return producto
        return None
    
    def esta_vacio(self) -> bool:
        """Verifica si el inventario está vacío"""
        return len(self._productos) == 0
import os

from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.archivo_servicio import ArchivoServicio


class RestauranteServicio:

    def __init__(self):
        ruta_base = os.path.dirname(
            os.path.dirname(os.path.abspath(__file__))
        )

        self.ruta_productos = os.path.join(
            ruta_base,
            "datos",
            "productos.json"
        )

        self.ruta_usuarios = os.path.join(
            ruta_base,
            "datos",
            "usuarios.json"
        )

    # =====================================================
    # USUARIOS
    # =====================================================

    def validar_usuario(self, usuario, password):
        usuarios = ArchivoServicio.leer_json(
            self.ruta_usuarios
        )

        for datos in usuarios:
            if (
                datos.get("usuario") == usuario
                and datos.get("password") == password
            ):
                return True

        return False

    def obtener_usuarios(self):
        datos = ArchivoServicio.leer_json(
            self.ruta_usuarios
        )

        usuarios = []

        for item in datos:
            usuario = Usuario(
                item.get("usuario", ""),
                item.get("password", "")
            )

            usuarios.append(usuario)

        return usuarios

    # =====================================================
    # PRODUCTOS
    # =====================================================

    def obtener_productos(self):
        datos = ArchivoServicio.leer_json(
            self.ruta_productos
        )

        productos = []

        for item in datos:
            producto = Producto(
                item.get("id"),
                item.get("nombre", ""),
                item.get("precio", 0),
                item.get("categoria", "")
            )

            productos.append(producto)

        return productos

    def buscar_producto(self, id_producto):
        productos = self.obtener_productos()

        for producto in productos:
            if producto.id == id_producto:
                return producto

        return None

    def registrar_producto(self, producto):
        # Validaciones del negocio
        if producto.id <= 0:
            return False, "El ID debe ser mayor que cero."

        if producto.nombre.strip() == "":
            return False, "El nombre del producto es obligatorio."

        if producto.precio < 0:
            return False, "El precio no puede ser negativo."

        if producto.categoria.strip() == "":
            return False, "La categoría es obligatoria."

        productos = self.obtener_productos()

        # Verificar ID repetido
        for existente in productos:
            if existente.id == producto.id:
                return False, "Ya existe un producto con ese ID."

        productos.append(producto)

        self.guardar_productos(productos)

        return True, "Producto registrado correctamente."

    def actualizar_producto(self, producto_actualizado):
        # Validaciones del negocio
        if producto_actualizado.id <= 0:
            return False, "El ID debe ser mayor que cero."

        if producto_actualizado.nombre.strip() == "":
            return False, "El nombre del producto es obligatorio."

        if producto_actualizado.precio < 0:
            return False, "El precio no puede ser negativo."

        if producto_actualizado.categoria.strip() == "":
            return False, "La categoría es obligatoria."

        productos = self.obtener_productos()

        for i, producto in enumerate(productos):

            if producto.id == producto_actualizado.id:

                productos[i] = producto_actualizado

                self.guardar_productos(productos)

                return True, "Producto actualizado correctamente."

        return False, "No existe un producto con ese ID."

    def eliminar_producto(self, id_producto):
        productos = self.obtener_productos()

        for i, producto in enumerate(productos):

            if producto.id == id_producto:

                productos.pop(i)

                self.guardar_productos(productos)

                return True, "Producto eliminado correctamente."

        return False, "No existe un producto con ese ID."

    # =====================================================
    # PERSISTENCIA DE PRODUCTOS
    # =====================================================

    def guardar_productos(self, productos):

        datos = []

        for producto in productos:
            datos.append(
                producto.to_dict()
            )

        ArchivoServicio.guardar_json(
            self.ruta_productos,
            datos
        )
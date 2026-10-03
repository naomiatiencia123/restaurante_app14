import tkinter as tk
from tkinter import ttk, messagebox

from modelos.producto import Producto
from servicios.restaurante_servicio import RestauranteServicio


class MainView:

    def __init__(self, root):
        self.root = root
        self.servicio = RestauranteServicio()

        self.root.title("Restaurante App")
        self.root.geometry("950x650")
        self.root.minsize(850, 550)

        self.crear_interfaz()
        self.mostrar_productos()

    # =====================================================
    # INTERFAZ PRINCIPAL
    # =====================================================

    def crear_interfaz(self):

        # Contenedor principal
        contenedor = ttk.Frame(
            self.root,
            padding=15
        )

        contenedor.pack(
            fill="both",
            expand=True
        )

        # Título
        titulo = ttk.Label(
            contenedor,
            text="RESTAURANTE APP",
            font=("Arial", 20, "bold")
        )

        titulo.pack(
            pady=(0, 15)
        )

        # Zona principal
        zona_principal = ttk.Frame(
            contenedor
        )

        zona_principal.pack(
            fill="both",
            expand=True
        )

        zona_principal.columnconfigure(
            1,
            weight=1
        )

        zona_principal.rowconfigure(
            0,
            weight=1
        )

        # =================================================
        # MENÚ DE NAVEGACIÓN
        # =================================================

        menu = ttk.LabelFrame(
            zona_principal,
            text="Navegación",
            padding=15
        )

        menu.grid(
            row=0,
            column=0,
            padx=(0, 15),
            sticky="ns"
        )

        ttk.Button(
            menu,
            text="Usuarios",
            command=self.mostrar_usuarios
        ).pack(
            fill="x",
            pady=5
        )

        ttk.Button(
            menu,
            text="Productos",
            command=self.mostrar_productos
        ).pack(
            fill="x",
            pady=5
        )

        # =================================================
        # CONTENIDO
        # =================================================

        self.contenido = ttk.Frame(
            zona_principal
        )

        self.contenido.grid(
            row=0,
            column=1,
            sticky="nsew"
        )

        self.contenido.columnconfigure(
            0,
            weight=1
        )

        self.contenido.rowconfigure(
            2,
            weight=1
        )

    # =====================================================
    # LIMPIAR CONTENIDO
    # =====================================================

    def limpiar_contenido(self):

        for widget in self.contenido.winfo_children():
            widget.destroy()

    # =====================================================
    # PRODUCTOS
    # =====================================================

    def mostrar_productos(self):

        self.limpiar_contenido()

        titulo = ttk.Label(
            self.contenido,
            text="Gestión de productos",
            font=("Arial", 16, "bold")
        )

        titulo.grid(
            row=0,
            column=0,
            pady=(0, 10),
            sticky="w"
        )

        # =================================================
        # FORMULARIO
        # =================================================

        formulario = ttk.LabelFrame(
            self.contenido,
            text="Datos del producto",
            padding=15
        )

        formulario.grid(
            row=1,
            column=0,
            sticky="ew",
            pady=(0, 10)
        )

        formulario.columnconfigure(
            1,
            weight=1
        )

        # ID
        ttk.Label(
            formulario,
            text="ID:"
        ).grid(
            row=0,
            column=0,
            padx=5,
            pady=5,
            sticky="w"
        )

        self.entrada_id = ttk.Entry(
            formulario
        )

        self.entrada_id.grid(
            row=0,
            column=1,
            padx=5,
            pady=5,
            sticky="ew"
        )

        # Nombre
        ttk.Label(
            formulario,
            text="Nombre:"
        ).grid(
            row=1,
            column=0,
            padx=5,
            pady=5,
            sticky="w"
        )

        self.entrada_nombre = ttk.Entry(
            formulario
        )

        self.entrada_nombre.grid(
            row=1,
            column=1,
            padx=5,
            pady=5,
            sticky="ew"
        )

        # Precio
        ttk.Label(
            formulario,
            text="Precio:"
        ).grid(
            row=2,
            column=0,
            padx=5,
            pady=5,
            sticky="w"
        )

        self.entrada_precio = ttk.Entry(
            formulario
        )

        self.entrada_precio.grid(
            row=2,
            column=1,
            padx=5,
            pady=5,
            sticky="ew"
        )

        # Categoría
        ttk.Label(
            formulario,
            text="Categoría:"
        ).grid(
            row=3,
            column=0,
            padx=5,
            pady=5,
            sticky="w"
        )

        self.entrada_categoria = ttk.Entry(
            formulario
        )

        self.entrada_categoria.grid(
            row=3,
            column=1,
            padx=5,
            pady=5,
            sticky="ew"
        )

        # =================================================
        # BOTONES
        # =================================================

        botones = ttk.Frame(
            formulario
        )

        botones.grid(
            row=4,
            column=0,
            columnspan=2,
            pady=(10, 0)
        )

        ttk.Button(
            botones,
            text="Registrar",
            command=self.registrar_producto
        ).grid(
            row=0,
            column=0,
            padx=5
        )

        ttk.Button(
            botones,
            text="Cargar",
            command=self.cargar_producto
        ).grid(
            row=0,
            column=1,
            padx=5
        )

        ttk.Button(
            botones,
            text="Actualizar",
            command=self.actualizar_producto
        ).grid(
            row=0,
            column=2,
            padx=5
        )

        ttk.Button(
            botones,
            text="Eliminar",
            command=self.eliminar_producto
        ).grid(
            row=0,
            column=3,
            padx=5
        )

        ttk.Button(
            botones,
            text="Limpiar",
            command=self.limpiar_formulario
        ).grid(
            row=0,
            column=4,
            padx=5
        )

        # =================================================
        # TABLA
        # =================================================

        tabla_frame = ttk.LabelFrame(
            self.contenido,
            text="Productos registrados",
            padding=10
        )

        tabla_frame.grid(
            row=2,
            column=0,
            sticky="nsew"
        )

        tabla_frame.columnconfigure(
            0,
            weight=1
        )

        tabla_frame.rowconfigure(
            0,
            weight=1
        )

        self.tabla_productos = ttk.Treeview(
            tabla_frame,
            columns=(
                "id",
                "nombre",
                "precio",
                "categoria"
            ),
            show="headings"
        )

        self.tabla_productos.heading(
            "id",
            text="ID"
        )

        self.tabla_productos.heading(
            "nombre",
            text="Nombre"
        )

        self.tabla_productos.heading(
            "precio",
            text="Precio"
        )

        self.tabla_productos.heading(
            "categoria",
            text="Categoría"
        )

        self.tabla_productos.column(
            "id",
            width=80,
            anchor="center"
        )

        self.tabla_productos.column(
            "nombre",
            width=220
        )

        self.tabla_productos.column(
            "precio",
            width=100,
            anchor="center"
        )

        self.tabla_productos.column(
            "categoria",
            width=160
        )

        self.tabla_productos.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        scrollbar = ttk.Scrollbar(
            tabla_frame,
            orient="vertical",
            command=self.tabla_productos.yview
        )

        scrollbar.grid(
            row=0,
            column=1,
            sticky="ns"
        )

        self.tabla_productos.configure(
            yscrollcommand=scrollbar.set
        )

        self.cargar_tabla_productos()

    # =====================================================
    # OBTENER PRODUCTO DEL FORMULARIO
    # =====================================================

    def obtener_datos_formulario(self):

        id_texto = self.entrada_id.get().strip()
        nombre = self.entrada_nombre.get().strip()
        precio_texto = self.entrada_precio.get().strip()
        categoria = self.entrada_categoria.get().strip()

        # Comprobar campos vacíos
        if (
            id_texto == ""
            or nombre == ""
            or precio_texto == ""
            or categoria == ""
        ):
            messagebox.showwarning(
                "Datos incompletos",
                "Complete todos los campos del producto."
            )

            return None

        # Convertir ID
        try:
            id_producto = int(id_texto)
        except ValueError:
            messagebox.showerror(
                "Error",
                "El ID debe ser un número entero."
            )

            return None

        # Convertir precio
        try:
            precio = float(precio_texto)
        except ValueError:
            messagebox.showerror(
                "Error",
                "El precio debe ser un número."
            )

            return None

        return Producto(
            id_producto,
            nombre,
            precio,
            categoria
        )

    # =====================================================
    # REGISTRAR
    # =====================================================

    def registrar_producto(self):

        producto = self.obtener_datos_formulario()

        if producto is None:
            return

        resultado, mensaje = self.servicio.registrar_producto(
            producto
        )

        if resultado:

            messagebox.showinfo(
                "Registro exitoso",
                mensaje
            )

            self.limpiar_formulario()
            self.cargar_tabla_productos()

        else:

            messagebox.showerror(
                "No se pudo registrar",
                mensaje
            )

    # =====================================================
    # CARGAR
    # =====================================================

    def cargar_producto(self):

        id_texto = self.entrada_id.get().strip()

        if id_texto == "":
            messagebox.showwarning(
                "Dato requerido",
                "Ingrese el ID del producto."
            )

            return

        try:
            id_producto = int(id_texto)
        except ValueError:
            messagebox.showerror(
                "Error",
                "El ID debe ser un número entero."
            )

            return

        producto = self.servicio.buscar_producto(
            id_producto
        )

        if producto is None:

            messagebox.showerror(
                "Producto no encontrado",
                "No existe un producto con ese ID."
            )

            return

        self.entrada_nombre.delete(
            0,
            tk.END
        )

        self.entrada_nombre.insert(
            0,
            producto.nombre
        )

        self.entrada_precio.delete(
            0,
            tk.END
        )

        self.entrada_precio.insert(
            0,
            str(producto.precio)
        )

        self.entrada_categoria.delete(
            0,
            tk.END
        )

        self.entrada_categoria.insert(
            0,
            producto.categoria
        )

    # =====================================================
    # ACTUALIZAR
    # =====================================================

    def actualizar_producto(self):

        producto = self.obtener_datos_formulario()

        if producto is None:
            return

        resultado, mensaje = self.servicio.actualizar_producto(
            producto
        )

        if resultado:

            messagebox.showinfo(
                "Actualización exitosa",
                mensaje
            )

            self.limpiar_formulario()
            self.cargar_tabla_productos()

        else:

            messagebox.showerror(
                "No se pudo actualizar",
                mensaje
            )

    # =====================================================
    # ELIMINAR
    # =====================================================

    def eliminar_producto(self):

        id_texto = self.entrada_id.get().strip()

        if id_texto == "":
            messagebox.showwarning(
                "Dato requerido",
                "Ingrese el ID del producto."
            )

            return

        try:
            id_producto = int(id_texto)
        except ValueError:
            messagebox.showerror(
                "Error",
                "El ID debe ser un número entero."
            )

            return

        producto = self.servicio.buscar_producto(
            id_producto
        )

        if producto is None:

            messagebox.showerror(
                "Producto no encontrado",
                "No existe un producto con ese ID."
            )

            return

        confirmar = messagebox.askyesno(
            "Confirmar eliminación",
            "¿Está seguro de eliminar este producto?"
        )

        if not confirmar:
            return

        resultado, mensaje = self.servicio.eliminar_producto(
            id_producto
        )

        if resultado:

            messagebox.showinfo(
                "Eliminación exitosa",
                mensaje
            )

            self.limpiar_formulario()
            self.cargar_tabla_productos()

        else:

            messagebox.showerror(
                "No se pudo eliminar",
                mensaje
            )

    # =====================================================
    # CARGAR TABLA
    # =====================================================

    def cargar_tabla_productos(self):

        for item in self.tabla_productos.get_children():
            self.tabla_productos.delete(item)

        productos = self.servicio.obtener_productos()

        for producto in productos:

            self.tabla_productos.insert(
                "",
                "end",
                values=(
                    producto.id,
                    producto.nombre,
                    f"{producto.precio:.2f}",
                    producto.categoria
                )
            )

    # =====================================================
    # LIMPIAR FORMULARIO
    # =====================================================

    def limpiar_formulario(self):

        self.entrada_id.delete(
            0,
            tk.END
        )

        self.entrada_nombre.delete(
            0,
            tk.END
        )

        self.entrada_precio.delete(
            0,
            tk.END
        )

        self.entrada_categoria.delete(
            0,
            tk.END
        )

    # =====================================================
    # USUARIOS
    # =====================================================

    def mostrar_usuarios(self):

        self.limpiar_contenido()

        titulo = ttk.Label(
            self.contenido,
            text="Consulta de usuarios",
            font=("Arial", 16, "bold")
        )

        titulo.grid(
            row=0,
            column=0,
            pady=(0, 10),
            sticky="w"
        )

        usuarios_frame = ttk.LabelFrame(
            self.contenido,
            text="Usuarios registrados",
            padding=10
        )

        usuarios_frame.grid(
            row=1,
            column=0,
            sticky="nsew"
        )

        self.contenido.rowconfigure(
            1,
            weight=1
        )

        usuarios_frame.columnconfigure(
            0,
            weight=1
        )

        usuarios_frame.rowconfigure(
            0,
            weight=1
        )

        tabla_usuarios = ttk.Treeview(
            usuarios_frame,
            columns=(
                "usuario",
                "password"
            ),
            show="headings"
        )

        tabla_usuarios.heading(
            "usuario",
            text="Usuario"
        )

        tabla_usuarios.heading(
            "password",
            text="Contraseña"
        )

        tabla_usuarios.column(
            "usuario",
            width=200
        )

        tabla_usuarios.column(
            "password",
            width=200
        )

        tabla_usuarios.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        usuarios = self.servicio.obtener_usuarios()

        for usuario in usuarios:

            tabla_usuarios.insert(
                "",
                "end",
                values=(
                    usuario.usuario,
                    usuario.password
                )
            )
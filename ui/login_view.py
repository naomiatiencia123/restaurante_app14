import tkinter as tk
from tkinter import ttk, messagebox

from servicios.restaurante_servicio import RestauranteServicio


class LoginView:

    def __init__(self, root):

        self.root = root
        self.servicio = RestauranteServicio()

        self.root.title(
            "Restaurante App - Inicio de sesión"
        )

        self.root.geometry(
            "400x400"
        )

        self.root.resizable(
            False,
            False
        )

        self.crear_interfaz()

    # =====================================================
    # INTERFAZ
    # =====================================================

    def crear_interfaz(self):

        contenedor = ttk.Frame(
            self.root,
            padding=30
        )

        contenedor.pack(
            fill="both",
            expand=True
        )

        titulo = ttk.Label(
            contenedor,
            text="Restaurante App",
            font=("Arial", 20, "bold")
        )

        titulo.pack(
            pady=(10, 5)
        )

        subtitulo = ttk.Label(
            contenedor,
            text="Inicio de sesión"
        )

        subtitulo.pack(
            pady=(0, 20)
        )

        formulario = ttk.LabelFrame(
            contenedor,
            text="Acceso",
            padding=20
        )

        formulario.pack(
            fill="x"
        )

        formulario.columnconfigure(
            1,
            weight=1
        )

        # Usuario
        ttk.Label(
            formulario,
            text="Usuario:"
        ).grid(
            row=0,
            column=0,
            padx=5,
            pady=8,
            sticky="w"
        )

        self.entrada_usuario = ttk.Entry(
            formulario
        )

        self.entrada_usuario.grid(
            row=0,
            column=1,
            padx=5,
            pady=8,
            sticky="ew"
        )

        # Contraseña
        ttk.Label(
            formulario,
            text="Contraseña:"
        ).grid(
            row=1,
            column=0,
            padx=5,
            pady=8,
            sticky="w"
        )

        self.entrada_password = ttk.Entry(
            formulario,
            show="*"
        )

        self.entrada_password.grid(
            row=1,
            column=1,
            padx=5,
            pady=8,
            sticky="ew"
        )

        # Botón
        ttk.Button(
            contenedor,
            text="Ingresar",
            command=self.iniciar_sesion
        ).pack(
            pady=25
        )

    # =====================================================
    # LOGIN
    # =====================================================

    def iniciar_sesion(self):

        usuario = self.entrada_usuario.get().strip()
        password = self.entrada_password.get().strip()

        if usuario == "" or password == "":
            messagebox.showwarning(
                "Datos incompletos",
                "Ingrese usuario y contraseña."
            )

            return

        acceso = self.servicio.validar_usuario(
            usuario,
            password
        )

        if acceso:

            messagebox.showinfo(
                "Acceso correcto",
                "Bienvenido al sistema."
            )

            self.abrir_principal()

        else:

            messagebox.showerror(
                "Acceso denegado",
                "Usuario o contraseña incorrectos."
            )

    # =====================================================
    # ABRIR VENTANA PRINCIPAL
    # =====================================================

    def abrir_principal(self):

        self.root.destroy()

        nueva_ventana = tk.Tk()

        from ui.main_view import MainView

        MainView(
            nueva_ventana
        )

        nueva_ventana.mainloop()
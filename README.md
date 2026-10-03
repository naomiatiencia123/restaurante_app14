# Restaurante App
JAMIE NAOMI ATIENCIA VASQUEZ
## Semana 14 - Componentes y contenedores

Aplicación de escritorio desarrollada en Python utilizando Tkinter y ttk
para la gestión básica de un restaurante.

En esta Semana 14 se mejoró la interfaz gráfica del proyecto mediante el
uso de componentes, contenedores y gestores de geometría de Tkinter.

## Objetivo

El objetivo es permitir la gestión de productos de un restaurante mediante
una interfaz gráfica organizada, manteniendo la arquitectura modular y la
persistencia de información mediante archivos JSON.

La aplicación permite iniciar sesión, consultar usuarios y gestionar
productos.

## Tecnologías utilizadas

- Python 3
- Tkinter
- ttk
- JSON
- Programación Orientada a Objetos (POO)

## Estructura del proyecto

```text
restaurante_app14/
├── datos/
│   ├── productos.json
│   └── usuarios.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── usuario.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
├── ui/
│   ├── __init__.py
│   ├── login_view.py
│   └── main_view.py
├── assets/
├── main.py
└── README.md
import json


class ArchivoServicio:

    @staticmethod
    def leer_json(ruta):
        try:
            with open(ruta, "r", encoding="utf-8") as archivo:
                return json.load(archivo)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    @staticmethod
    def guardar_json(ruta, datos):
        with open(ruta, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)
class Usuario:
    def __init__(self, usuario, password):
        self.usuario = usuario
        self.password = password

    def to_dict(self):
        return {
            "usuario": self.usuario,
            "password": self.password
        }
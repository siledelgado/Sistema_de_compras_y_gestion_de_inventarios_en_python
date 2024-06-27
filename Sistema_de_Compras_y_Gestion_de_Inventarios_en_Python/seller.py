from user import User

# Definir la clase Seller que hereda de User
class Seller(User):
    # Inicializar la clase Seller
    def __init__(self, name):
        # Llamar al constructor de la clase base (User) para inicializar el nombre
        super().__init__(name)


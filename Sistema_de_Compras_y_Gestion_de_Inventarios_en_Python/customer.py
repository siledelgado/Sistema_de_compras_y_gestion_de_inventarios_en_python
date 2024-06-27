from user import User  # Importa la clase User desde el módulo user
from cart import Cart  # Importa la clase Cart desde el módulo cart

class Customer(User):
    
    def __init__(self, name):
        super().__init__(name)  # Inicializa la clase base User con el nombre proporcionado
        self.cart = Cart(self)  # Cuando se crea una instancia de Customer, tiene un carrito asociado con él mismo como propietario

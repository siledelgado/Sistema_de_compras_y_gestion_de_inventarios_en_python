# Importamos la clase Wallet del módulo wallet
from wallet import Wallet

class User:
    # Importamos los métodos show_items, items_list y pick_items del módulo item_manager
    from item_manager import show_items, items_list, pick_items, show_items

    def __init__(self, name):
        # Inicializamos la instancia de User con un nombre
        self.name = name
        # Creamos una instancia de Wallet, estableciendo el User (self) como el propietario
        self.wallet = Wallet(self)
        # La instancia de User o cualquier instancia de una clase que herede de User
        # tendrá una billetera que se crea con el User como propietario cuando se instancia.

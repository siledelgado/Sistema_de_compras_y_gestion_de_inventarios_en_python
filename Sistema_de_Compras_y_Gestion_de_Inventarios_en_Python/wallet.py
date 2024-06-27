class Wallet:
    # Importamos el método 'set_owner' del módulo 'ownable'
    from ownable import set_owner

    def __init__(self, owner):
        # Inicializamos la billetera con el propietario especificado
        # usando el método 'set_owner' importado.
        self.set_owner(owner)
        # Inicializamos el balance de la billetera a 0.
        self.balance = 0

    def deposit(self, amount):
        # Convertimos el monto a un entero y lo agregamos al balance.
        self.balance += int(amount)

    def withdraw(self, amount):
        # Verificamos si el balance es mayor o igual al monto que se quiere retirar.
        if not self.balance >= amount:
            # Si no es así, no hacemos nada (salimos del método).
            return
        # Si el balance es suficiente, convertimos el monto a un entero
        # y lo restamos del balance.
        self.balance -= int(amount)
        # Devolvemos el monto retirado.
        return amount


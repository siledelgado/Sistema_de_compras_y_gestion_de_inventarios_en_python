class Cart:
    from item_manager import show_items  # Importa la función show_items desde el módulo item_manager
    from ownable import set_owner  # Importa la función set_owner desde el módulo ownable

    def __init__(self, owner):
        self.set_owner(owner)  # Establece el propietario del carrito
        self.items = []  # Inicializa una lista vacía para almacenar los ítems del carrito

    def items_list(self):
        return self.items  # Retorna la lista de ítems del carrito

    def add(self, item):
        self.items.append(item)  # Agrega un ítem al carrito

    def total_amount(self):
        price_list = []
        for item in self.items:
            price_list.append(item.price)
        return sum(price_list)  # Calcula y retorna el monto total de todos los ítems en el carrito

    def check_out(self):
        if self.owner.wallet.balance < self.total_amount():
            print("Saldo insuficiente. Transacción cancelada.")
            return

        # Transferir el precio de compra de todos los artículos del carrito al monedero del propietario de cada artículo
        for item in self.items:
            withdrawn_amount = self.owner.wallet.withdraw(item.price)

            if withdrawn_amount is not None:
                item.owner.wallet.deposit(withdrawn_amount)  # Deposita el monto retirado en el monedero del propietario del artículo
                item.owner = self.owner  # Transfiere la propiedad del artículo al propietario del carrito

        # Vacía el contenido del carrito después de la compra
        self.items = []

        print("Compra realizada con éxito.")

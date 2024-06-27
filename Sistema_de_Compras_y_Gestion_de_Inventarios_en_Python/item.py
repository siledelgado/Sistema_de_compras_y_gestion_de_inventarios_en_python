class Item:
    instances = []  # Lista para almacenar todas las instancias de Item

    def __init__(self, name, price, owner=None):
        self.name = name  # Nombre del ítem
        self.price = price  # Precio del ítem
        self.set_owner(owner)  # Método para establecer el propietario del ítem
        Item.instances.append(self)  # Añade esta instancia a la lista de instancias

    def label(self):
        return {"name": self.name, "price": self.price}
        # Retorna un diccionario con el nombre y el precio del ítem

    @staticmethod
    def item_all():
        # Método estático para obtener todas las instancias de Item creadas hasta el momento
        return Item.instances

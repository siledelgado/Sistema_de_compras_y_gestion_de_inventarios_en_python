# Importar las clases Customer (Cliente), Item (Artículo) y Seller (Vendedor) desde sus respectivos módulos
from customer import Customer
from item import Item
from seller import Seller

# Crear una instancia de Seller (Vendedor) con el nombre "Tienda DIC"
seller = Seller("Tienda DIC")

# Generar 10 productos para el vendedor (Seller)
for i in range(10):
    Item("CPU", 40830, seller)  # Crear 10 instancias del artículo CPU con precio 40830
    Item("Memoria RAM", 13880, seller)  # Crear 10 instancias del artículo Memoria RAM con precio 13880
    Item("Placa Madre", 28980, seller)  # Crear 10 instancias del artículo Placa Madre con precio 28980
    Item("Fuente de Poder", 8980, seller)  # Crear 10 instancias del artículo Fuente de Poder con precio 8980
    Item("Caja de PC", 8727, seller)  # Crear 10 instancias del artículo Caja de PC con precio 8727
    Item("Disco Duro 3.5 pulgadas", 10980, seller)  # Crear 10 instancias del artículo Disco Duro 3.5 pulgadas con precio 10980
    Item("SSD 2.5 pulgadas", 13370, seller)  # Crear 10 instancias del artículo SSD 2.5 pulgadas con precio 13370
    Item("SSD M.2", 12980, seller)  # Crear 10 instancias del artículo SSD M.2 con precio 12980
    Item("Enfriador de CPU", 13400, seller)  # Crear 10 instancias del artículo Enfriador de CPU con precio 13400
    Item("Tarjeta Gráfica", 23800, seller)  # Crear 10 instancias del artículo Tarjeta Gráfica con precio 23800

# Solicitar al usuario su nombre y crear una instancia de Customer (Cliente) con ese nombre
print("🤖 Por favor, dime tu nombre")
customer = Customer(input())  # Recibir el nombre del cliente

# Solicitar al usuario cargar dinero en su billetera y realizar el depósito
print("🏧 Por favor, ingresa la cantidad a cargar en tu billetera")
customer.wallet.deposit(int(input()))  # Recibir y depositar el monto en la billetera del cliente

# Iniciar el proceso de compra
print("🛍️ Empieza a comprar")
end_shopping = False  # Variable para controlar el fin de la compra
while not end_shopping:
    # Mostrar la lista de productos disponibles
    print("📜 Lista de productos")
    seller.show_items()  # Mostrar los productos disponibles

    # Solicitar al usuario el número y la cantidad de productos a comprar
    print("️️⛏ Por favor, ingresa el número del producto")
    number = int(input())  # Recibir el número del producto
    print("⛏ Por favor, ingresa la cantidad del producto")
    quantity = int(input())  # Recibir la cantidad del producto

    # Seleccionar los artículos del vendedor y agregarlos al carrito del cliente
    items = seller.pick_items(number, quantity)  # Seleccionar los productos del vendedor
    for item in items:
        customer.cart.add(item)  # Agregar los productos al carrito del cliente

    # Mostrar el contenido actual del carrito y el total
    print("🛒 Contenido del carrito")
    customer.cart.show_items()  # Mostrar el contenido del carrito
    print(f"🤑 Monto total: {customer.cart.total_amount()}")  # Mostrar el monto total de los productos en el carrito

    # Preguntar al usuario si desea terminar de comprar
    print("😭 ¿Quieres terminar de comprar? (sí/no)")
    end_shopping = input().lower() == "sí"  # Finalizar la compra si el usuario ingresa "sí"

# Preguntar al usuario si desea confirmar la compra y realizar el proceso de check-out si es el caso
print("💸 ¿Quieres confirmar tu compra? (sí/no)")
if input().lower() == "sí":
    customer.cart.check_out()  # Confirmar la compra

# Mostrar resultados finales: propiedad del cliente, saldo de su billetera, estado del inventario del vendedor y su saldo de billetera, contenido final del carrito y su cantidad total
print("୨୧┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈ Resultado ┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈୨୧")
print(f"️🛍️ ️Propiedades de {customer.name}:")
customer.show_items()  # Mostrar los artículos en posesión del cliente
print(f"😱👛 Saldo de billetera de {customer.name}: {customer.wallet.balance}")  # Mostrar el saldo de la billetera del cliente

print(f"📦 Estado del inventario de {seller.name}:")
seller.show_items()  # Mostrar el estado del inventario del vendedor
print(f"😻👛 Saldo de billetera de {seller.name}: {seller.wallet.balance}")  # Mostrar el saldo de la billetera del vendedor

print("🛒 Contenido final del carrito")
customer.cart.show_items()  # Mostrar el contenido final del carrito del cliente
print(f"🌚 Monto total: {customer.cart.total_amount()}")  # Mostrar el monto total del carrito

print("🎉 Fin")  # Finalizar el programa

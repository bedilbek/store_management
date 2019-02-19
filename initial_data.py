from models.Order import Order
from models.Store import Store
from models.Product import Product
from models.Staff import Staff
from models.Customer import Customer

stores = [
    Store(1, "IUT-WebStore Management System", "Deutga", "156-25-63"),
]

staffs = [
    Staff("Jaiden", "Tashkent", "123465", 12, "Cashier", 5600),
    Staff("Humongus", "Balls", "965412", 15, "Guard", 7600)
]

customers = [
    Customer("5632879", "Dave", "Dventiliga", 256, 10, "589-44-85", ["Wings", "Golden"]),
    Customer("9653287", "Gustavo", "Feritana", 25, 562, "555-44-44", ["Premium"])
]

products = [
    Product(123456, "Chocolate Flavor", "Cookies with chocolate", 25, 1),
    Product(954687, "Meat", "Tasty meat", 50, 5),
    Product(248984, "Brick", "It is just a brick", 900, 3),
    Product(967485, "Secret sause", "Special secret Krabsburger sause", 150, 2),
    Product(336599, "Stick", "Stick for real man", 10, 4)
]

orders = [
    Order(stores[0], customers[0], staffs[0], [{Order.PRODUCT_KEY:product[0], Order.QUANTITY_KEY: product[1]}
                                               for product in [(products[0], 2), (products[1], 3), (products[2], 1)]]),
]


from Store import Store
from Product import Product
from Staff import Staff
from Order import Order
from Customer import Customer
import os

stores = [
    Store(1, "Travic", "Deutga", "156-25-63"),
    Store(2, "Zatzu", "Wakanda", "693-95-19"),
    Store(3, "Korzinka", "Tashkent", "596-27-03")
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
    Product("123456", "Chocolate Flavor", "Cookies with chocolate", 25, 1),
    Product("954687", "Meat", "Tasty meat", 50, 5),
    Product("248984", "Brick", "It is just a brick", 900, 3),
    Product("967485", "Secret sause", "Special secret Krabsburger sause", 150, 2),
    Product("336599", "Stick", "Stick for real man", 10, 4)
]


def cls():
    os.system('cls' if os.name=='nt' else 'clear')    

def select(items):
    for i,s in enumerate(items):
        print(f'{i + 1}. {s}')
    i = int(input())
    while(i > len(items)):
        print('Wrong input!')
        i = int(input())
    return i - 1

def createCustomer():
    print("Create Customer")
    print("ID:")
    id = input()
    print("Name:")
    name = input()
    print("SSN:")
    ssn = input()
    print("Address:")
    address = input()
    print("Tel:")
    tel = input()
    cls()
    return Customer(ssn, name, address, id, 0, tel, [])

def createStaff():
    print("Job title:")
    jobTitle = input()
    print("ID: {}")
    id = input()
    print("Name: {}")
    name = input()
    print("SSN: {}")
    ssn = input()
    print("Address: {}")
    address = input()
    print("Salary: {}")
    salary = input()
    cls()
    return Staff(name, address, ssn, id, jobTitle, salary)

order = Order()
selectedStore = 0
selectedProducts = []
selectedCustomer = 0
selectedStaff = 0

menu = [
    ['Select Store', stores],
    ['Add Product', products],
    ['Remove Products', selectedProducts],
    ['Select Customer', customers],
    ['Select Staff', staffs],
    ['Create Customer', customers],
    ['Create Staff', customers],
    ['Create Order', order]
]
selectedIndex = 0
while(True):
    for i, m in enumerate(menu):
        print(f'{i + 1}. {m[0]}')
    print('Select Menu: ')
    i = int(input())
    while(i > len(menu)):
        print('Wrong input!')
        i = int(input())
    cls()
    if i != 3 and i != 6 and i != 7 and i != 8:
        s = select(menu[i-1][1])
    cls()
    if i == 1:
        selectedStore = menu[i-1][1][s]
    elif i == 2:
        print("Quantity: ")
        q = input()
        selectedProducts.append({
            Order.PRODUCT_KEY: menu[i-1][1][s],
            Order.QUANTITY_KEY: q
        })
    elif i == 3:
        selectedProducts.clear()
    elif i == 4:
        selectedCustomer = menu[i-1][1][s]
    elif i == 5:
        selectedStaff = menu[i-1][1][s]
    elif i == 6:
        customer = createCustomer()
        customers.append(customer)
        print(customer)
    elif i == 7:
        staff = createStaff()
        staffs.append(staff)
        print(staff)
    elif i == 8:
        order = Order(selectedStore, selectedCustomer, selectedStaff, selectedProducts)
        cls()
        print(order)
        break
        

    
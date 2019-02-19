from models.staff import Staff
from models.order import Order
from models.customer import Customer
from initial_data import products, customers, staffs, stores
import os


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
        


import datetime
from xmlrpc.client import DateTime

from models.store import Store
from models.staff import Staff
from models.customer import Customer


class Order:
    PRODUCT_KEY = "product"
    QUANTITY_KEY = "quantity"

    def __init__(self, storeObject=None, customerObject=None, staffObject=None, productObjects=None):
        if all(item is not None for item in [storeObject, customerObject, staffObject, productObjects]):
            self.storeObject = storeObject
            self.customerObject = customerObject
            self.staffObject = staffObject
            self.productObjects = list(map(lambda pD: pD[Order.PRODUCT_KEY], productObjects))
            self.quantity = list(map(lambda pD: pD[Order.QUANTITY_KEY], productObjects))
            self.__date_created = datetime.datetime.now()

    def __str__(self):
        out_center_width = 100
        header_welcome = f'Welcome to {self.storeObject.name}:'.center(out_center_width)
        header_staff = f'Staff: {self.staffObject.name}'.center(out_center_width)
        header_customer = f'Customer ID: {self.customerObject.id}'.center(out_center_width)
        header_receipt = 'RECEIPT'.center(out_center_width)

        header = header_welcome + '\n' + header_staff + '\n' + header_customer + '\n\n' + header_receipt + '\n'

        subheader_date = '{}'.format(self.date_created.strftime("%d/%m/%Y")).center(out_center_width)
        subheader_time = '{}'.format(self.date_created.strftime("%H:%M:%S")).center(out_center_width)

        subheader = subheader_date + '\n' + subheader_time + '\n' + '\n\n'

        total_cost = sum(map(lambda p: p.price, self.productObjects))
        total_points = sum(map(lambda p: p.points, self.productObjects))

        body = 'Product Name\tProduct Code\tPrice\tQuantity\n'
        bill = [f'{product.name:^10}\t{product.productCode:^10}\t{product.price:^7}\t{self.quantity[index]:^12}' for index, product in enumerate(self.productObjects)]
        body = (body + '\n'.join(bill)).expandtabs(20)
        body += '\n\n\n'

        footer_total = f'TOTAL:\t{total_cost}'.expandtabs(out_center_width)
        footer_items_sold = f'# ITEMS SOLD {sum(self.quantity)}'.center(out_center_width)
        footer_total_points = f'Total points: {total_points}'
        footer_customer_copy = f'***CUSTOMER COPY***'.center(out_center_width)


        footer = footer_total + '\n\n' + footer_items_sold + '\n\n' + footer_total_points + '\n\n' + footer_customer_copy

        return  header + subheader + body + footer

    def addProduct(self, product):
        self.productObjects.append(product)

    def setStoreObject(self, storeObject):
        if isinstance(storeObject, Store):
            self.__storeObject = storeObject

    def setCustomerObject(self, customerObject):
        if isinstance(customerObject, Customer):
            self.__customerObject = customerObject

    def setStuffObject(self, staffObject):
        if isinstance(staffObject, Staff):
            self.__staffObject = staffObject

    def setProductObjects(self, productObjects):
        self.__productObjects = productObjects

    def setQuantity(self, quantity):
        try:
            quantities = list(map(int, quantity))
        except:
            raise TypeError('quantity - Expected int, Actual' + str(type(quantity)))
        if any([q <= 0 for q in quantities]):
            raise ValueError('quantity - Should be no less than 1')
        self.__quantity = quantities

    def getStoreObject(self):
        return self.__storeObject

    def getCustomerObject(self):
        return self.__customerObject

    def getStuffObject(self):
        return self.__staffObject

    def getProductObject(self):
        return self.__productObjects

    def getQuantity(self):
        return self.__quantity

    def getDateCreated(self):
        return self.__date_created

    storeObject = property(getStoreObject, setStoreObject)
    customerObject = property(getCustomerObject, setCustomerObject)
    staffObject = property(getStuffObject, setStuffObject)
    productObjects = property(getProductObject, setProductObjects)
    quantity = property(getQuantity, setQuantity)
    date_created = property(getDateCreated)

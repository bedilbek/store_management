from Store import Store
from Staff import Staff
from Product import Product
from Customer import Customer
from functools import reduce
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

    def __str__(self):
        pOut = "\tProducts:\nName\tCode\tPrice\tQuantity\n"
        for i,p in enumerate(self.productObjects):
            pOut += "%s\t%s\t%s\t%s" % (p.name, p.productCode, p.price, self.quantity[i]) + "\n"
        pOut = pOut.expandtabs(30)
        
        totalcost = sum(map(lambda p: p.price, self.productObjects))
        totalPoints = sum(map(lambda p: p.points, self.productObjects))
        stOut = "Store: \n\tName: %s\n\tID: %s\n\tAddress: %s\n\tTel: %s" % (self.storeObject.name, self.storeObject.id, self.storeObject.address, self.storeObject.tel)
        staOut = "%s:\n\tID: %s\n\tName: %s" % (self.staffObject.jobTitle, self.staffObject.id, self.staffObject.name)
        cOut = "Customer:\n\tID: %s" % (self.customerObject.id)
        out = "%s\n%s\n%s\n%s\nTotal Cost: %s\nTotal Points: %s" % (stOut, staOut, cOut, pOut, totalcost, totalPoints)
        return out

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
        self.__quantity = quantity

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

    storeObject = property(getStoreObject, setStoreObject)
    customerObject = property(getCustomerObject, setCustomerObject)
    staffObject = property(getStuffObject, setStuffObject)
    productObjects = property(getProductObject, setProductObjects)
    quantity = property(getQuantity, setQuantity)
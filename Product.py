class Product:
    def __init__(self, productCode, name, description, price, points):
        self.productCode = productCode
        self.name = name
        self.description = description
        self.price = price
        self.points = points

    def __str__(self):
        out = f"Product:\
            \n\tName: {self.name}\
            \n\tProduct Code: {self.productCode}\
            \n\tDescription: {self.description}\
            \n\tPoints: {self.points}\
            \n\tPoints: {self.price}"
        return out

    def setProductCode(self, productCode):
        self.__productCode = productCode
    
    def setName(self, name):
        self.__name = name
    
    def setDescription(self, description):
        self.__description = description

    def setPrice(self, price):
        self.__price = price

    def setPoints(self, points):
        if isinstance(points, int):
            self.__points = points
        else:
            raise TypeError("Expected Int for Points")

    def getProductCode(self):
        return self.__productCode 
    
    def getName(self):
        return self.__name 
    
    def getDescription(self):
        return self.__description 

    def getPrice(self):
        return self.__price 

    def getPoints(self):
        return self.__points 

    productCode = property(getProductCode, setProductCode)
    name = property(getName, setName)
    description = property(getDescription, setDescription)
    price = property(getPrice, setPrice)
    points = property(getPoints, setPoints)
from typing import Union


class Product:
    def __init__(self, productCode: int, name: str, description: str, price:Union[float, int], points: int):
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

    def setProductCode(self, productCode: int):
        if not isinstance(productCode, int):
            raise TypeError(productCode="Expected: int, Actual: " + str(type(productCode)))
        if productCode < 1:
            raise ValueError(productCode="Should be not less than 1")
        self.__productCode = productCode
    
    def setName(self, name: str):
        if len(name.strip()) < 1:
            raise ValueError(name="Should be at least length of 1")
        self.__name = name
    
    def setDescription(self, description: str):
        if len(description.strip()) < 1:
            raise ValueError(name="Should be at least length of 1")
        self.__description = description

    def setPrice(self, price: Union[float, int]):
        if not isinstance(price, float) and not isinstance(price, int):
            raise TypeError(price="Expected: int or float, Actual: " + str(type(price)))
        if price < 0.001:
            raise ValueError(price="Should be not less than 0.001")
        self.__price = price

    def setPoints(self, points):
        if not isinstance(points, int):
            raise TypeError(points="Expected: int, Actual" + str(type(points)))
        if points < 1:
            raise ValueError(points="Should be not less than 1")
        self.__points = points

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

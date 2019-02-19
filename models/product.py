from typing import Union


class Product:
    def __init__(self, productCode: int, name: str, description: str, price: Union[float, int], points: int):
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
        final = None
        try:
            final = int(productCode)
        except:
            raise TypeError(f'product_code - Expected: int, Actual: {str(type(productCode))}')
        if final < 1:
            raise ValueError(f'productCode - Should be not less than 1')
        self.__productCode = final

    def setName(self, name: str):
        if len(name.strip()) < 1:
            raise ValueError("name - Should be at least length of 1")
        self.__name = name

    def setDescription(self, description: str):
        if len(description.strip()) < 1:
            raise ValueError("description - Should be at least length of 1")
        self.__description = description

    def setPrice(self, price: Union[float, int]):
        final = None
        try:
            final = float(price)
        except:
            raise TypeError("price - Expected: int or float, Actual: " + str(type(price)))

        if final < 0.001:
            raise ValueError("price - Should be not less than 0.001")
        self.__price = final

    def setPoints(self, points):
        final = None
        try:
            final = int(points)
        except:
            raise TypeError("points - Expected: int, Actual" + str(type(points)))

        if final < 1:
            raise ValueError("points - Should be not less than 1")
        self.__points = final

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

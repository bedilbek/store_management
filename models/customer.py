from models.citizen import Citizen


class Customer(Citizen):
    def __init__(self, ssn, name, address, id, purchasingPoints, tel, memberships):
        super().__init__(ssn, name, address)
        self.id = id
        self.purchasingPoints = purchasingPoints
        self.tel = tel
        self.memberships = memberships

    def __str__(self):
        out = f"Customer:\
            \n\tID: {self.id}\
            \n\tName: {self.name}\
            \n\tSSN: {self.ssn}\
            \n\tAddress: {self.address}\
            \n\tMemberships: {self.memberships}\
            \n\tPurchasing Points: {self.purchasingPoints}\
            \n\tTel: {self.tel}"
        return out

    def setId(self, id):
        self.__id = id

    def setPurchasingPoints(self, purchasingPoints):
        if isinstance(purchasingPoints, int):
            self.__purchasingPoints = purchasingPoints
        else:
            raise TypeError("Expected Int value for Purchasing points")

    def setTel(self, tel):
        self.__tel = tel

    def setMemberships(self, memberships):
        if isinstance(memberships, list) and all([isinstance(x, str) for x in memberships]):
            self.__memberships = memberships
        else:
            raise TypeError("Expected [String] value for Memberships")

    def getId(self):
        return self.__id

    def getPurchasingPoints(self):
        return self.__purchasingPoints
    
    def getTel(self):
        return self.__tel

    def getMemberships(self):
        return self.__memberships

    id = property(getId, setId)
    purchasingPoints = property(getPurchasingPoints, setPurchasingPoints)
    tel = property(getTel, setTel)
    memberships = property(getMemberships, setMemberships)

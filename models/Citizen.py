class Citizen:
    def __init__(self, ssn, name, address):
        self.ssn = ssn
        self.name = name
        self.address = address

    def __str__(self):
        return super().__str__()

    def getName(self):
        return self.__name

    def getAddr(self):
        return self.__address

    def getSsn(self):
        return self.__ssn
    
    def setName(self, name):
        self.__name = name

    def setAddr(self, address):
        self.__address = address

    def setSsn(self, ssn):
        self.__ssn = ssn

    name = property(getName, setName)
    ssn = property(getSsn, setSsn)
    address = property(getAddr, setAddr)


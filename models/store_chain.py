class StoreChain:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def getName(self):
        return self.__name

    def getAddr(self):
        return self.__address

    def setName(self, name):
        self.__name = name

    def setAddr(self, address):
        self.__address = address

    name = property(getName, setName)
    address = property(getAddr, setAddr)

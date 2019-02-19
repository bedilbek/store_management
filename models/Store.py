from models.StoreChain import StoreChain

class Store(StoreChain):
    def __init__(self, id, name, address, tel):
        super().__init__(name, address)
        self.id = id
        self.tel = tel

    def __str__(self):
        out = f'Store:\
            \n\tName: {self.name}\
            \n\tID: {self.id}\
            \n\tAddress: {self.address}\
            \n\tTel: {self.tel}'
        return out

    def getId(self):
        return self.__id

    def getTel(self):
        return self.__tel

    def setId(self, id):
        self.__id = id

    def setTel(self, tel):
        self.__tel = tel

    tel = property(getTel, setTel)
    id = property(getId, setId)

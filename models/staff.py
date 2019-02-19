from models.citizen import Citizen


class Staff(Citizen):
    def __init__(self, name, address, ssn, id, jobTitle, salary):
        super().__init__(ssn, name, address)
        self.id = id
        self.jobTitle = jobTitle
        self.salary = salary

    def __str__(self):
        out = f"{self.jobTitle}:\
            \n\tID: {self.id}\
            \n\tName: {self.name}\
            \n\tSSN: {self.ssn}\
            \n\tAddress: {self.address}\
            \n\tSalary: {self.salary}"
        return out

    def getId(self):
        return self.__id

    def getJobTitle(self):
        return self.__jobTitle

    def getSalary(self):
        return self.__salary

    def setId(self, id):
        self.__id = id

    def setJobTitle(self, jobTitle):
        self.__jobTitle = jobTitle

    def setSalary(self, salary):
        self.__salary = salary

    id = property(getId, setId)
    jobTitle = property(getJobTitle, setJobTitle)
    salary = property(getSalary, setSalary)

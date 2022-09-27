class Employee:
    def __init__(self,name,IdNumber,department,jobTitle,monthlySalary):
        self.__name = name
        self.__IdNumber = IdNumber
        self.__department = department
        self.__jobTitle = jobTitle
        self.__monthlySalary = monthlySalary

    def getName(self):
        return self.__name
    def getIdNumber(self):
        return self.__IdNumber
    def getDepartment(self):
        return self.__department
    def getJobTitle(self):
        return self.__jobTitle
    def getMonthlySalary(self):
        return self.__monthlySalary

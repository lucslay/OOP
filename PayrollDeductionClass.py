class PayrollDeduction:
    def __init__(self,description,date,chargeAmount,employeeID):
        self.__description = description
        self.__date = date
        self.__chargeAmount = chargeAmount
        self.__employeeID = employeeID

    def get_desciption(self):
        return self.__description

    def get_date(self):
        return self.__date

    def get_chargeAmount(self):
        return self.__chargeAmount

    def get_employeeID(self):
        return self.__employeeID
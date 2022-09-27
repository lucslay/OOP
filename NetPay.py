import EmployeeClass as emp
import PayrollDeductionClass as prd

def main():
    emp1 = emp.Employee("Jimmy Smith", 58475, "Information Systems", "Developer", 6800.00)

    deduction1 = prd.PayrollDeduction("food court","8/14/2022",22.50,39119)
    deduction2 = prd.PayrollDeduction("gift contribution","8/12/2022",25.00,58475)
    deduction3 = prd.PayrollDeduction("food court","8/17/2022",15.25,21547)
    deduction4 = prd.PayrollDeduction("vending machine","8/22/2022",3.00,58475)
    deduction5 = prd.PayrollDeduction("vending machine","8/5/2022",2.75,58475)

    salary = emp1.getMonthlySalary()
    charge1 = deduction1.get_chargeAmount()
    charge2 = deduction2.get_chargeAmount()
    charge3 = deduction3.get_chargeAmount()
    charge4 = deduction4.get_chargeAmount()
    charge5 = deduction5.get_chargeAmount()

    netPay = salary - charge1 - charge2 - charge3 - charge4 - charge5
    theMonthlySalary = emp1.getMonthlySalary()
    print("*** Employee Pay ***")
    print("Name: ", emp1.getName())
    print("IDNumber: ", emp1.getIdNumber())
    print("Department: ", emp1.getDepartment())
    print("Gross Pay: $", '{0:.2f}'.format(theMonthlySalary), sep = '')
    print("Net Pay: $",'{0:.2f}'.format(netPay), sep = '')

main()
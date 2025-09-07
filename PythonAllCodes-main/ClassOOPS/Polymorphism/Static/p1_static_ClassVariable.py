class Employee:
    company_name = "Infosys"   # class variable (shared across instances)

    def __init__(self, name):
        self.name = name  # instance variable (unique to each instance)


amit = Employee("Amit")
print(amit.company_name)
amit2 = Employee("Amit2")
amit3 = Employee("Amit3")
amit4 = Employee("Amit4")
amit5 = Employee("Amit5")
print(amit2.company_name)
print(amit3.company_name)
print(amit4.company_name)
print(amit5.company_name)   

class Employee:
    company_name = "ETC Solutions"  # class variable

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_company(cls, new_name):
        cls.company_name = new_name  # cls means access to class variable

# Create employees
e1 = Employee("Suraj")
e2 = Employee("Amit")

# Before change
print(e1.company_name)  # ETC Solutions
print(e2.company_name)  # ETC Solutions

# Change company name using class method
Employee.change_company("OpenAI India")

# After change
print(e1.company_name)  # OpenAI India
print(e2.company_name)  # OpenAI India
